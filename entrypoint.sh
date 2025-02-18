#!/bin/sh

while ! nc -z $MYSQL_HOST "${MYSQL_PORT:-3306}"; do
  sleep 1
done

python manage.py migrate mysite

python manage.py migrate

python manage.py collectstatic --noinput

exec gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
