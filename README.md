# Proyecto con Django: Appriendo

Este proyecto es una applicación web desarrollada con Django, Incluye operaciones CRUD (crear, leer, actualizar y eliminar) y está conectado a una base de datos PostgreSQL.
Tiene el objetivo de crear un espacio vitual en el que arrendatarios y arrendadores puedan tanto publicar sus sitios en renta, como elegir cómoda y confiadamente los lugares que quieran rentar con mejor detalle. Originalmente pensado para estudiantes universitarios que viven lejos de sus universidades, y necesitan un sitio confiable donde encontrar sus necesidades sin perder el tiempo.

Tecnologías utilizadas
- Python 3.12
- Django 5.2.8
- PostgreSQL
- HTML, CSS y JavaScript

Requisitos de ejecución
- Python instalado
- PostgreSQL instalado y base de datos creada
- Entorno virtual


Instalación
1. Crear y activar el entorno virtual:
   python -m venv venv
   source venv/bin/activate  (Windows: venv\Scripts\activate)

2. Instalar dependencias:
   pip install -r requirements.txt

3. Configurar la base de datos en settings.py.

4. Ejecutar migraciones:
   python manage.py migrate

5. Ejecutar el servidor:
   python manage.py runserver
