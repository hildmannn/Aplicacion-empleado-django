# Aplicación de Gestión de Empleados en Django

Esta es una aplicación web desarrollada en Django para gestionar empleados. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los datos de los empleados, así como otras funcionalidades relacionadas con la gestión de recursos humanos.

## Tecnologías Utilizadas

- **Backend**: Django
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML, CSS, Foundation

## Instalación

### Prerrequisitos

- **Python 3.6 o superior**
- **pip** (gestor de paquetes de Python)
- **virtualenv** (opcional pero recomendado)
- **Paquetes de Python necesarios**:
  - asgiref 3.8.1
  - Django 5.0.4
  - django-js-asset 2.2.0
  - pillow 10.3.0
  - psycopg2 2.9.9
  - sqlparse 0.4.4
  - tzdata 2024.1
  - pip 24.0
  - setuptools 65.5.0

### Pasos de Instalación

1. Clona el repositorio
   ```bash
   git clone https://github.com/hildmannn/Aplicacion-empleado-django.git
   cd Aplicacion-empleado-django

2. Crea un entorno virtual y actívalo
   python -m venv env
   source env/bin/activate  # En Windows usa `env\Scripts\activate`

3. Instala las dependencias mencionadas en los prerrequisitos
  pip install asgiref==3.8.1 Django==5.0.4 django-js-asset==2.2.0 pillow==10.3.0 psycopg2==2.9.9 sqlparse==0.4.4 tzdata==2024.1 pip==24.0 setuptools==65.5.0

4. Configura la base de datos PostgreSQL
   Asegúrate de tener PostgreSQL instalado y configurado. Crea una base de datos para la aplicación y ajusta las configuraciones de la base de datos en el archivo settings.py.
   
5 Realiza las migraciones de la base de datos
  python manage.py migrate

6. Crea un superusuario para acceder al panel de administración
   python manage.py createsuperuser

7. Ejecuta el servidor de desarrollo
   python manage.py runserver

8. Accede a la aplicación en tu navegador web
   http://127.0.0.1:8000/


Contacto
Autor: Valentin Hildmann
Email: hildmannvalentin@gmail.com





