#!/usr/bin/env sh

if [ "$#" = 0 ]
then
    python -m pip freeze
fi

postgres_ready() {
python << END
from sys import exit
from psycopg2 import connect, OperationalError
try:
    connect(
        dbname="${DB_NAME}",
        user="${DB_USER}",
        password="${DB_PASSWORD}",
        host="${DB_HOST}",
    )
except OperationalError as error:
    print(error)
    exit(-1)
exit(0)
END
}

until postgres_ready; do
    >&2 echo "Postgres is unavailable - sleeping"
    sleep 3
done;

>&2 echo "Postgres is available"

if [ "$#" = 0 ]
then
    >&2 echo "No command detected; running default commands"
    >&2 echo "Running migrations"
    python manage.py migrate --noinput
    >&2 echo "\n\nStarting development server: 127.0.0.1:8000\n\n"
    python manage.py runserver_plus --cert-file /ssl-certs/cert.crt 0.0.0.0:8000
else
    >&2 echo "Command detected; running command"
    exec "$@"
fi
