Intall packages from requirements:
    pip install -r requirements.txt
    pip install django-bootstrap4

Chamge om /:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME':'hbdb',
        'USER': 'xime',
        'PASSWORD': 'root',
        'HOST':'localhost',
        'PORT':'5432',
    }
}
    
Activate virtual environment:
    source activate DjangoProject

Run server:
    python manage.py runserver

    
-----------
Create DB
$sudo -i -u postgres psql
postgres=# CREATE USER “your_username” WITH PASSWORD “your_pass”;
postgres=# CREATE DATABASE teste_django WITH OWNER your_username;

python manage.py makemigrations
python manage.py migrate


user: xime
pass: root
----------------
ADMIM

user: ximenAs
pass: 123456A.

--------------

Links:
http://127.0.0.1:8000/register/
http://127.0.0.1:8000/login/
http://127.0.0.1:8000/contentuser/progress
http://127.0.0.1:8000/contentuser/team
