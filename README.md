# Project example python django

## stack

- python 3.10
- django
- python-dotenv
- mysql
- docker
- tailwind flowbite cdn (cms)
- pyjwt

## extension

- rest client (doc api)

## init project and app

```
$django-admin startproject [project_name]
$python manage.py startapp [app_name]
$pip freeze > requirements.txt

$python -m venv venv (split environment)
(on mac) $venv/bin/activate
(on windows) $source venv/Scripts/activate
*** when not implement venv, use deactivate to exit venv

$pip install -r requirements.txt
```

## setup

```
## setup database
$python manage.py makemigrations
$python manage.py migrate

## setup env
$cp .env.example .env

## how to run
$python manage.py runserver

## how to run on docker
$docker-compose up -d
```

## Setup admin django

```
## create superuser admin django
$python manage.py createsuperuser
```

## rollback db

```
$python manage.py migrate [app_name] zero (rollback to zero)
$python manage.py migrate [app_name] [file_migrate_name] (rollback to last migrate)
```

## clear log admin

```
$python manage.py shell
$from django.contrib.admin.models import LogEntry
$LogEntry.objects.all().delete()
$exit()
```
