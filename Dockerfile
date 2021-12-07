# syntax = docker/dockerfile:experimental
FROM        python:3.9-slim

# Language, Timezone
ENV         LANG C.UTF-8

RUN         --mount=type=cache,target=/var/cache/apt --mount=type=cache,target=/var/lib/apt \
            apt -y update &&\
            apt -y dist-upgrade &&\
            apt -y autoremove

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
CMD         python manage.py shell_plus --ipython
