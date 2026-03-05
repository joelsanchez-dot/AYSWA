# AYSWA - Sistema de Gestión Académica

Sistema Django para gestión académica con módulos de alumnos, productos, apartados e inscripciones.

## 📋 Requisitos

- Python 3.8+
- Django 5.2.11
- pip (gestor de paquetes)

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/varmich1/AYSWA.git
cd AYSWA
```

### 2. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/macOS
python -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
cd SISTEMA
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tus valores específicos
# Mínimo cambiar: SECRET_KEY, DEBUG
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (administrador)

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en: `http://localhost:8000`

Panel administrativo: `http://localhost:8000/admin`

## 📁 Estructura del Proyecto

```
SISTEMA/
├── manage.py                 # Script de gestión de Django
├── requirements.txt          # Dependencias del proyecto
├── .env.example             # Variables de entorno de ejemplo
├── SISTEMA/                 # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py          # Configuraciones principales
│   ├── urls.py              # Rutas principales
│   ├── asgi.py              # Configuración ASGI (producción)
│   └── wsgi.py              # Configuración WSGI (producción)
├── apartados/               # App: Apartados
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── templates/
│   │   └── apartados/
│   │       ├── home.html
│   │       ├── producto_list.html
│   │       ├── producto_form.html
│   │       └── producto_delete.html
│   └── migrations/
├── alumnos/                 # App: Alumnos
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
├── alumna_jazmin/           # App: Alumna Jazmín
│   └── migrations/
├── inscripciones/           # App: Inscripciones
│   └── migrations/
└── productos/               # App: Productos
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── Productos/
    │       ├── index.html
    │       └── editar.html
    └── migrations/
```

## 🔧 Funcionalidades

- **Apartados**: Gestión de apartados (CRUD)
- **Alumnos**: Gestión de información de alumnos
- **Productos**: Gestión de productos
- **Inscripciones**: Sistema de inscripciones

## 🔐 Seguridad

- Variables de entorno para datos sensitivos
- DEBUG desactivado en producción
- SECRET_KEY protegida
- ALLOWED_HOSTS configurado

### Checklist de Seguridad

Antes de deployar a producción:

- [ ] Cambiar `SECRET_KEY` en `.env` por una clave fuerte y aleatoria
- [ ] Establecer `DEBUG=False` en `.env`
- [ ] Configurar `ALLOWED_HOSTS` con tu dominio
- [ ] Usar HTTPS
- [ ] Configurar una base de datos robusta (PostgreSQL recomendado)
- [ ] Ejecutar `python manage.py collectstatic` para assets estáticos
- [ ] Configurar email para recuperación de contraseña
- [ ] Usar un gestor secretos (no .env en producción)

## 📝 Comandos Útiles

```bash
# Crear nuevas migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword username

# Recolectar archivos estáticos (producción)
python manage.py collectstatic

# Ejecutar servidor (desarrollo)
python manage.py runserver

# Ejecutar servidor en puerto específico
python manage.py runserver 0.0.0.0:8080

# Crear backup de base de datos
python manage.py dumpdata > backup.json

# Restaurar backup
python manage.py loaddata backup.json
```

## 🧪 Testing (Opcional)

```bash
# Ejecutar tests
python manage.py test

# Con cobertura
python manage.py test --verbosity=2
```

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'django'"

```bash
pip install -r requirements.txt
```

### Error: "Database migration problems"

```bash
python manage.py migrate --run-syncdb
```

### Error: "Static files not loading"

```bash
python manage.py collectstatic --noinput
```

### Limpiar caché de Python

```bash
# Eliminar directorios __pycache__
find . -type d -name __pycache__ -exec rm -rf {} +

# Eliminar archivos .pyc
find . -type f -name "*.pyc" -delete
```

## 📦 Deployment

### Con Gunicorn + Nginx

```bash
# Instalar Gunicorn
pip install gunicorn

# Ejecutar con Gunicorn
gunicorn SISTEMA.wsgi:application --bind 0.0.0.0:8000
```

### Con Docker (Opcional)

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "SISTEMA.wsgi:application", "--bind", "0.0.0.0:8000"]
```

## 🤝 Contribuciones

1. Fork el repositorio
2. Crea tu rama (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo licencia MIT. Ver archivo LICENSE para más detalles.

## 📧 Contacto

Para preguntas o problemas, abre un issue en el repositorio de GitHub.

---

**Última actualización**: Marzo 2026  
**Versión**: 1.0.0  
**Estado**: En Desarrollo
