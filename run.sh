#!/bin/bash
python3 /code/manage.py migrate
python3 /code/manage.py createsuperuser --username='admin' --email='admin@mail.com' --no-input
python3 /code/manage.py collectstatic --noinput
python3 /code/manage.py runserver 0.0.0.0:8000
