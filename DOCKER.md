# Running Development Server in Docker

### Running PostgreSQL Database in a Docker Container

Instead of installing a database server on your local computer, it is worth considering running a database
in a Docker container. Everything remains the same, as if you were running the application locally, except
that the database now runs in the Docker container. 

The container runs the PostgreSQL database image 12.9-bullseye. It runs 12.9 version of the
Postgres database, and it is based on Debian Bullseye. 

The Docker setup is defined in **docker-compose-postgres.yml** file.
The environment variables are defined in **docker-postgres.env** file. The variables
defined in the file can be modified, as per needs and requirements, or the file can be used as is.

Running Postgres database container:

    docker-compose -f docker-compose-postgres.yml --env-file=./docker/postgres/docker-postgres.env up


### Running Application Development Server in a Docker Container

The application containers can be started with the command:

    docker-compose up 

For implementation details see:

1) docker-compose.yml: docker compose file
2) docker/django/Dockerfile: Dockerfile that allows to assemble Django application image
3) docker/django/entrypoint.sh: Shell script specifying application entry point.

