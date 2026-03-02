from datetime import date, datetime, timedelta
from django.db import models
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    GrupoEscolar, Asignacion, InscripcionGrupo,
    SesionClase, Asistencia
)

ESTADOS = [
    ("P", "Presente"),
    ("A", "Ausente"),
    ("R", "Retardo"),
    ("J", "Justificado"),
]

def home(request):
    # Lista de grupos para iniciar
    grupos = GrupoEscolar.objects.all().order_by("clave")
    return render(request, "asistencias/home.html", {"grupos": grupos})

@login_required
def pasar_lista(request, grupo_id):
    grupo = get_object_or_404(GrupoEscolar, id=grupo_id)

    asignaciones = (
        Asignacion.objects.filter(grupo=grupo, activa=True)
        .select_related("materia", "docente")
        .order_by("materia__nombre")
    )

    # Para selector: últimas sesiones del grupo (últimas 25)
    ultimas_sesiones = (
        SesionClase.objects.filter(asignacion__grupo=grupo)
        .select_related("asignacion__materia", "asignacion__docente")
        .order_by("-fecha", "-bloque")[:25]
    )

    # --- Crear/Abrir sesión ---
    if request.method == "POST" and request.POST.get("accion") == "abrir_sesion":
        asignacion_id = int(request.POST["asignacion_id"])
        fecha_str = request.POST["fecha"]
        bloque = int(request.POST["bloque"])

        # VALIDACIÓN LUN–VIE
        fecha_dt = datetime.fromisoformat(fecha_str).date()
        if fecha_dt.weekday() > 4:
            return render(
                request,
                "asistencias/pasar_lista.html",
                {
                    "grupo": grupo,
                    "asignaciones": asignaciones,
                    "ultimas_sesiones": ultimas_sesiones,
                    "sesion": None,
                    "asistencias": [],
                    "hoy": date.today().isoformat(),
                    "estados": ESTADOS,
                    "error": "Solo se permite pasar lista de lunes a viernes.",
                },
            )

        asignacion = get_object_or_404(Asignacion, id=asignacion_id, grupo=grupo)

        # Crear sesión única por asignación+fecha+bloque
        sesion, _ = SesionClase.objects.get_or_create(
            asignacion=asignacion,
            fecha=fecha_str,
            bloque=bloque,
        )

        # Crear asistencia default (Ausente) para todos los alumnos inscritos activos
        inscripciones = (
            InscripcionGrupo.objects.filter(grupo=grupo, activa=True)
            .select_related("alumno")
        )
        for ins in inscripciones:
            Asistencia.objects.get_or_create(
                sesion=sesion,
                alumno=ins.alumno,
                defaults={"estado": "A"},
            )

        return redirect(f"/grupo/{grupo.id}/pasar-lista/?sesion={sesion.id}")

    # --- Si ya hay sesión seleccionada, mostrar lista ---
    sesion = None
    asistencias = []
    sesion_id = request.GET.get("sesion")

    if sesion_id:
        sesion = get_object_or_404(SesionClase, id=sesion_id, asignacion__grupo=grupo)
        asistencias = (
            Asistencia.objects.filter(sesion=sesion)
            .select_related("alumno")
            .order_by("alumno__nombre")
        )

        # Guardar cambios
        if request.method == "POST" and request.POST.get("accion") == "guardar":
            for a in asistencias:
                nuevo = request.POST.get(f"estado_{a.id}")
                comentario = request.POST.get(f"comentario_{a.id}", "")
                if nuevo in {"P", "A", "R", "J"}:
                    a.estado = nuevo
                    a.comentario = comentario.strip()
                    a.save()
            return redirect(f"/grupo/{grupo.id}/pasar-lista/?sesion={sesion.id}")

    return render(
        request,
        "asistencias/pasar_lista.html",
        {
            "grupo": grupo,
            "asignaciones": asignaciones,
            "ultimas_sesiones": ultimas_sesiones,
            "sesion": sesion,
            "asistencias": asistencias,
            "hoy": date.today().isoformat(),
            "estados": ESTADOS,
        },
    )

def _lunes_de_semana(fecha: date) -> date:
    # weekday(): 0=Lun ... 6=Dom
    return fecha - timedelta(days=fecha.weekday())


def _viernes_de_semana(fecha: date) -> date:
    return _lunes_de_semana(fecha) + timedelta(days=4)


def _fin_de_mes(fecha: date) -> date:
    inicio = fecha.replace(day=1)
    if inicio.month == 12:
        sig = inicio.replace(year=inicio.year + 1, month=1, day=1)
    else:
        sig = inicio.replace(month=inicio.month + 1, day=1)
    return sig - timedelta(days=1)

@login_required
def resumen(request, grupo_id):
    grupo = get_object_or_404(GrupoEscolar, id=grupo_id)

    asignaciones = Asignacion.objects.filter(grupo=grupo, activa=True).select_related("materia", "docente").order_by("materia__nombre")
    asignacion_id = request.GET.get("asignacion")
    asignacion_sel = None
    if asignacion_id:
        asignacion_sel = get_object_or_404(Asignacion, id=asignacion_id, grupo=grupo)

    # Fecha base (default: hoy)
    fecha_str = request.GET.get("fecha", date.today().isoformat())
    try:
        fecha_base = datetime.fromisoformat(fecha_str).date()
    except ValueError:
        fecha_base = date.today()
        fecha_str = fecha_base.isoformat()

    # Rango semanal Lun–Vie
    inicio_sem = _lunes_de_semana(fecha_base)
    fin_sem = _viernes_de_semana(fecha_base)

    # Rango mensual
    inicio_mes = fecha_base.replace(day=1)
    fin_mes = _fin_de_mes(fecha_base)

    # Sesiones del grupo en cada rango
    sesiones_sem = SesionClase.objects.filter(
        asignacion__grupo=grupo,
        fecha__range=(inicio_sem, fin_sem),
    )
    if asignacion_sel:
        sesiones_sem = sesiones_sem.filter(asignacion=asignacion_sel)
        
    sesiones_mes = SesionClase.objects.filter(
        asignacion__grupo=grupo,
        fecha__range=(inicio_mes, fin_mes),
    )

    if asignacion_sel:
        sesiones_mes = sesiones_mes.filter(asignacion=asignacion_sel)

    # Estadísticas por alumno:
    # criterio de "asistió" = P + R + J (A no)
    def _stats(qs_sesiones):
        qs = (
            Asistencia.objects.filter(sesion__in=qs_sesiones)
            .values("alumno__matricula", "alumno__nombre")
            .annotate(
                total=Count("id"),
                presentes=Count("id", filter=models.Q(estado="P")),
                ausentes=Count("id", filter=models.Q(estado="A")),
                retardos=Count("id", filter=models.Q(estado="R")),
                justificados=Count("id", filter=models.Q(estado="J")),
            )
            .order_by("alumno__nombre")
        )

        rows = []
        for r in qs:
            total = r["total"] or 0
            asistio = (r["presentes"] + r["retardos"] + r["justificados"])
            porcentaje = (asistio / total * 100) if total else 0
            r["asistio"] = asistio
            r["porcentaje"] = round(porcentaje, 2)
            rows.append(r)
        return rows

    stats_sem = _stats(sesiones_sem)
    stats_mes = _stats(sesiones_mes)

    # Totales del grupo (por si tu profe lo pide)
    def _totales(stats):
        t = {"total": 0, "presentes": 0, "ausentes": 0, "retardos": 0, "justificados": 0, "asistio": 0}
        for r in stats:
            t["total"] += r["total"]
            t["presentes"] += r["presentes"]
            t["ausentes"] += r["ausentes"]
            t["retardos"] += r["retardos"]
            t["justificados"] += r["justificados"]
            t["asistio"] += r["asistio"]
        t["porcentaje"] = round((t["asistio"] / t["total"] * 100), 2) if t["total"] else 0
        return t

    tot_sem = _totales(stats_sem)
    tot_mes = _totales(stats_mes)

    return render(
        request,
        "asistencias/resumen.html",
        {
            "grupo": grupo,
            "fecha_base": fecha_base,
            "inicio_sem": inicio_sem,
            "fin_sem": fin_sem,
            "inicio_mes": inicio_mes,
            "fin_mes": fin_mes,
            "stats_sem": stats_sem,
            "stats_mes": stats_mes,
            "tot_sem": tot_sem,
            "tot_mes": tot_mes,
            "asignaciones": asignaciones,
            "asignacion_sel": asignacion_sel,
        },
    )
