# Assignment

Create vehicle registration API. Vehicle number pattern XXX000 (3 characters, 3 digits).
Use DjangoREST framework on the backend.

Requirements:
1) Vehicle number is unique
2) Vehicle number pattern must be validated

Applications user can

a) list all the vehicles;
b) add a new vehicle;
c) retrieve, edit, delete an existing vehicle.

Requirements:
1) There should be an opportunity to test the API functionality using front-end

Authorization has to be implemented.


# Implementation

### API Root

[http://localhost:8000/](http://localhost:8000/)


### List Vehicles / Create New 

[http://localhost:8000/vehicles/](http://localhost:8000/vehicles/)

### Edit / Update / Delete Vehicle

[http://localhost:8000/vehicles/vehicle_id/](http://localhost:8000/vehicles/<int:pk>/)

**Example:** Edit / Update / Delete Vehicle with id=1

[http://localhost:8000/vehicles/1/](http://localhost:8000/vehicles/1/)

### Django REST Browsable API

In order to test the API functionality one can use a web browser, thanks to DRF Browsable API feature.

### User Authentication

API supports:

a) Session Based Authentication;

Sample Account: 

username: registration_manager; password: good-day

b) Token Authentication;

Sample Account:

username: registration_manager; token: 59a0a6fea4760b89313a5ca595acf5d59cfd5099

### Pagination

Pagination has been implemented. The API returns the data in batches: it is not possible to 
retrieve all the data at once.

The default page size is 50. The maximum page size is set to 250.

[http://localhost:8000/vehicles/?offset=100&limit=200](http://localhost:8000/vehicles/?offset=100&limit=200)

The request above would pull the data of 200 vehicles starting from the vehicle 101 in the sequence.


### Search By Vehicle Number

Search by vehicle registration number has been implemented. 
Search criteria: vehicle number starts with.

** Example: **

[http://localhost:8000/vehicles/?search=ABC](http://localhost:8000/vehicles/?search=ABC)

### Comment

The development server can be run using the command

    python manage.py runserver

It is possible to run https development server

    python manage.py runserver_plus --cert-file cert.crt
