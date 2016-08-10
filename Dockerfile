FROM python:latest
ADD . .
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py collectstatic --noinput
CMD python3 manage.py runserver 0.0.0.0:8000

