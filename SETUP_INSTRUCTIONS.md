# Script de Limpieza y Configuración - AYSWA

## Paso 1: Verificar y Generar requirements.txt

```bash
# Ve a la raíz del proyecto
cd c:\Users\varmi\Documents\AYSWA\SISTEMA

# Verifica tu entorno virtual está activo
python -m pip list

# Genera requirements.txt
pip freeze > requirements.txt
```

**Contenido esperado** (ejemplo):
```
Django==4.2.0
djangorestframework==3.14.0
python-dotenv==0.21.0
```

## Paso 2: Crear archivo .env.example

Crear archivo `.env.example` en la raíz del proyecto (al lado de manage.py):

```env
# Django
DEBUG=False
SECRET_KEY=tu-clave-secreta-super-segura-aqui
ALLOWED_HOSTS=localhost,127.0.0.1,tu-dominio.com

# Database (si usas base de datos externa)
# DB_NAME=nombre_bd
# DB_USER=usuario
# DB_PASSWORD=contraseña
# DB_HOST=localhost
# DB_PORT=5432
```

## Paso 3: Actualizar settings.py

Reemplaza el código actual con configuración de variables de entorno:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# Ahora viene de variable de entorno
SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-p@u61ncpg5h)fm5qmbd&_k5%=l*imgj%6o0k5v+n(rygs7^cmi'
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = [
    h.strip() for h in os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')
]

# ... resto de la configuración
```

## Paso 4: Instalar python-dotenv (si no está instalado)

```bash
pip install python-dotenv
pip freeze > requirements.txt
```

## Paso 5: Crear .gitignore local para .env

El `.env` NUNCA debe estar en git (ya está en .gitignore):
```bash
# Verifica que esto esté en .gitignore
echo ".env" >> .gitignore
```

## Paso 6: Crear README.md

Crear archivo `README.md` en la raíz del proyecto:

```markdown
# AYSWA - Sistema de Gestión

Descripción del proyecto...

## Requisitos

- Python 3.8+
- Django 4.2
- (otras dependencias)

## Instalación

1. Clonar el repositorio
   \`\`\`bash
   git clone https://github.com/varmich1/AYSWA.git
   cd AYSWA
   \`\`\`

2. Crear entorno virtual
   \`\`\`bash
   python -m venv venv
   venv/Scripts/activate  # En Windows
   # source venv/bin/activate  # En Linux/Mac
   \`\`\`

3. Instalar dependencias
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Crear archivo .env
   \`\`\`bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   \`\`\`

5. Hacer migraciones
   \`\`\`bash
   python manage.py migrate
   \`\`\`

6. Crear superusuario
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

7. Ejecutar servidor
   \`\`\`bash
   python manage.py runserver
   \`\`\`

## Estructura del Proyecto

\`\`\`
SISTEMA/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── SISTEMA/              # Configuración del proyecto
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apartados/            # Aplicación de apartados
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   └── migrations/
├── alumnos/              # Aplicación de alumnos
│   └── ...
├── productos/            # Aplicación de productos
│   └── ...
└── inscripciones/        # Aplicación de inscripciones
    └── ...
\`\`\`

## Uso

Detalles sobre cómo usar el sistema...

## Contribuciones

Las contribuciones son bienvenidas...

## Licencia

Especificar licencia...
```

## Paso 7: Verificar y Hacer Commit

```bash
# Ver cambios
git status

# Agregar archivos
git add requirements.txt .env.example README.md
git add SISTEMA/settings.py  # Si actualizaste

# Commit
git commit -m "docs: agregar configuración y documentación del proyecto

- Crear requirements.txt con dependencias
- Crear .env.example para variables de entorno
- Crear README.md con instrucciones de instalación
- Actualizar settings.py para usar variables de entorno
- Mejorar seguridad usando SECRET_KEY y DEBUG desde .env"

# Push
git push origin productoss-michel
```

## Paso 8: Limpiar carpeta AYSWA/ (Opcional)

Si AYSWA/ es realmente obsoleta:

```bash
# Backup local (por si acaso)
mv AYSWA AYSWA_backup

# Eliminar de git
git rm -r AYSWA/
git commit -m "ci: eliminar estructura duplicada del proyecto"
git push origin productoss-michel
```

---

## Checklist Final

- [ ] requirements.txt creado y actualizado
- [ ] .env.example creado con configuraciones de ejemplo
- [ ] settings.py actualizado para usar variables de entorno
- [ ] .env creado localmente (NO en git)
- [ ] README.md creado con documentación
- [ ] Todos los cambios commiteados y pusheados
- [ ] Verificado que no hay archivos __pycache__ en git
- [ ] Verificado que .gitignore está correcto
- [ ] Base de datos (db.sqlite3) no está en git

---

## Troubleshooting

### Error: "No such file or directory: '.env'"
- Crea el archivo .env copiando de .env.example y editando

### Error en migrations
```bash
python manage.py migrate --run-syncdb
```

### Limpiar caché de Python
```bash
# Windows
Get-ChildItem -Path . -Include __pycache__ -Recurse | Remove-Item -Recurse -Force
Get-ChildItem -Path . -Include "*.pyc" -Recurse | Remove-Item -Force

# Linux/Mac
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type f -name "*.pyc" -delete
```
