# syntax = docker/dockerfile:experimental
FROM        python:3.12-slim

# Language, Timezone
ENV         LANG C.UTF-8

# requirements
COPY        requirements.txt /tmp/requirements.txt
RUN         --mount=type=cache,target=/root/.cache/pip \
            pip install -r /tmp/requirements.txt

# Create log directory
RUN         mkdir /var/log/gunicorn &&\
            mkdir /var/log/celery

COPY        .   /srv/
WORKDIR     /srv/playground

EXPOSE      8000
CMD         python manage.py shell_plus
