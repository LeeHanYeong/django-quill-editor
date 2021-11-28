#!/bin/sh

echo "Start development...";
set -xe;

poetry install;
poetry run python manage.py migrate;
poetry run python manage.py createsuperuser;

set +x

echo "Environment set. =)"
echo "in order to run django, please run: poetry run python manage.py runserver"