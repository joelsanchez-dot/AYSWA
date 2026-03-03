# 📚 AYSWA - Módulo Inventario Escolar

Sistema desarrollado en Django para la gestión de inventario escolar.

Incluye CRUD para:

- 💻 Computadoras  
- 🪑 Mobiliario  
- 📖 Biblioteca  

---

# ⚙️ Requisitos

Antes de ejecutar el proyecto debes tener instalado:

- Python 3.x
- pip
- Git (opcional)

---

# 🖥️ Verificar instalación

Verificar Python:

```bash
python --version
```

o

```bash
py --version
```

Verificar pip:

```bash
pip --version
```

---

# 📥 Clonar el proyecto

Ubicarse en la carpeta donde se desea guardar el proyecto:

```bash
cd Desktop
```

Clonar repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

Entrar al proyecto:

```bash
cd AYSWA/SISTEMA
```

⚠️ IMPORTANTE: Debes estar en la carpeta donde se encuentra el archivo `manage.py`.

---

# 📦 Instalar dependencias


```bash
pip install django
```

Verificar instalación:

```bash
python -m django --version
```

---

# 🗄️ Aplicar migraciones

```bash
python manage.py migrate
```

---

# 🚀 Ejecutar el servidor

Desde la carpeta donde está `manage.py`:

```bash
python manage.py runserver
```

El servidor iniciará en:

```
http://127.0.0.1:8000/
```

---

# 🔐 Acceso al Panel de Administración

Local:

```
http://127.0.0.1:8000/admin
```

---

# 👤 Superusuario Incluido

El archivo `db.sqlite3` está incluido en el repositorio, por lo tanto:

✅ Ya existe un superusuario creado.  
✅ No es necesario crear uno nuevo.  

Credenciales:

Username:
```
ToshioRonin
```

Password:
```
toshio199
```

---

# ➕ Crear un nuevo superusuario (Opcional)

Si se desea crear otro usuario administrador, ejecutar:

```bash
python manage.py createsuperuser
```

Y seguir las instrucciones en pantalla.

---

# 🌐 Acceder desde otra computadora (misma red)

1. Obtener IP local:

En Windows:

```bash
ipconfig
```

Buscar la dirección IPv4 (ejemplo: 192.168.1.15)

2. Ejecutar el servidor permitiendo conexiones externas:

```bash
python manage.py runserver 0.0.0.0:8000
```

3. Desde otra computadora ingresar en el navegador:

```
http://192.168.1.15:8000
```

(Reemplazar por tu IP real)

Para el panel de administrador:

```
http://TU_IP:8000/admin
```

---

# 🛠️ Estructura del Proyecto

```
AYSWA/
└── SISTEMA/
    ├── SISTEMA/
    ├── inventario/
    ├── db.sqlite3
    ├── manage.py
    └── README.md
```

---

# 📌 Notas Importantes

- El proyecto usa SQLite.
- La base de datos está incluida para facilitar la revisión académica.
- No usar esta configuración en producción.