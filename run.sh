#! /bin/bash
sleep 10
python3 /code/manage.py migrate
python3 /code/manage.py collectstatic --noinput
python3 /code/manage.py runserver 0.0.0.0:8000