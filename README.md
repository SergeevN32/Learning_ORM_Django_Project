# Movie Project

Тестовое приложение, представляющее из себя набор роутов для отображения различной информации о добавленных в БД фильмах и актерах, созданное для ознакомления с Django Object Relational Mapping, а так же с тестами встроенного в Django модуля TestCase

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Learning_ORM_Django_Project
    cd movie_app

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements/dev.txt

Run the app locally:

    python manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    pip install gunicorn
    gunicorn movie_proj.wsgi:application -b 0.0.0.0:8000
    
