# Zarnik Backend

Admin Panel with Django & Django rest framework

### creator: Abbas Rahimzadeh

* [Github](https://github.com/AAbbasRR)
* [Telegram](https://t.me/AAbbasRR)

## how to run:

install packages:

    1- create Virtualenv Environment Variable with command [python3 -m venv {virtual name}]
    2- active Virtualenv Environment Variable with command:
        windows: {virtual name}\Source\activate
        linux: source {virtual name}/bin/activate
    3- get project directory and install requirements packages with command [pip3 install -r requirements.txt

Config .env file:

    1- Create a file with name ".env" In the project directory, next to the file "main.py"
    2- Create 3 Variables:
        SECRET_KEY      -> str: a secret key for django project

create database:

    1- run command python manage.py makemigrations
    2- run command python manage.py migrate

create initial data`s:

    for create initial slider data`s: python manage.py createsliders
    for create initial section data`s: python manage.py createsections
    for create initial product data`s: python manage.py createproducts
    for create initial site settings data: python manage.py createsettings
    for create a superuser: python manage.py createsuperuser

run project:

    run command py runserver
    enter the url (127.0.0.1:8000) in your browser

## Enjoy...