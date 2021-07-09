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

[https://vehiclesapi.pythonanywhere.com](https://vehiclesapi.pythonanywhere.com)


### List All Vehicles / Create New 

[https://vehiclesapi.pythonanywhere.com/vehicles/](https://vehiclesapi.pythonanywhere.com/vehicles/)

### Edit / Update / Delete Vehicle

[https://vehiclesapi.pythonanywhere.com/vehicles/vehicle_id/](https://vehiclesapi.pythonanywhere.com/vehicles/<int:pk>/)

**Example:** Edit / Update / Delete Vehicle with id=1

[https://vehiclesapi.pythonanywhere.com/vehicles/1/](https://vehiclesapi.pythonanywhere.com/vehicles/1/)

### Django REST Browsable API

In order to test the API functionality one can use a web browser, thanks to DRF Browsable API feature.

### User Authentication

API supports:

a) Session Based Authentication;

Demo Account: 

username: **registration_manager**; password: *good-day**

b) Token Authentication;

Demo Account:

username: **registration_manager**; token: **c594ddd09fae0ead7c3969b51955be7aeb2c0163**

### Pagination

Pagination has been implemented. The API returns the data in batches: it is not possible to 
retrieve all the data at once.

The default page size is 50. The maximum page size is set to 250.

[https://vehiclesapi.pythonanywhere.com/vehicles/?offset=100&limit=200](https://vehiclesapi.pythonanywhere.com/vehicles/?offset=100&limit=200)

The request above would pull the data of 200 vehicles starting from the vehicle 101 in the sequence.


### Search By Vehicle Number

Search by vehicle registration number has been implemented. 
Search criteria: vehicle number starts with.

** Example: **

[https://vehiclesapi.pythonanywhere.com/vehicles/?search=ABC](https://vehiclesapi.pythonanywhere.com/vehicles/?search=ABC)

### Comment

The development server can be run using the command

    python manage.py runserver

It is possible to run https development server

    python manage.py runserver_plus --cert-file cert.crt
