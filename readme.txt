Lanera Fuhrmann SA - Desarrollo de Software - 2014
Carla Santos - Diego Carabajal - Matias Raies - Mariana Wheeler.

Instalación global
sudo pip install django

Configurar archivo local_settings.py con la base de datos ya creada en postgres. 

Posicionarse en la carpeta pFuhrmann/

Validación
python manage.py validate

Creación de tablas
python manage.py syncdb

Ejecutar FuhrmannSA
linea de comando: python manage.py runserver
abrir navegador: localhost:8000