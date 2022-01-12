FROM python:3.9-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED 1
RUN python -m pip install -U pip setuptools

RUN mkdir /ssl-certs

COPY requirements /tmp/requirements
RUN python -m pip install -U --no-cache-dir -r /tmp/requirements/requirements-dev.txt

COPY docker/django/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]