# Docker Development Container

You can run the application using pre-configured Docker container.
The container runs PostgreSQL database version 12.8, and pgAdmin4.

The container is defined in **docker-compose.yml** file.

In order to run the container you need to create an enviroment file,
let's call it **.dockernv**, where you have to define all the enviromental
variables mentioned in **docker-compose.yml**.

Finally, you need to adjust the Django application settings, to make it
consume the PostgreSQL database running in the container. 

As per current Docker setup, PostgreSQL database is running on port 
**5432**, on IP address **192.168.0.2**; the pgAdmin4 is running on 
port **80**, on IP address **192.168.0.3**.

