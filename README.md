Created a Functional REST CRUD API using Django, Django rest framework

PROJECT SETUP

Create a base folder

    a. Create a virtual environment using the command 'virtualenv venv' in the base

    b. install all dependencies including django and django rest framework in the virtual env

    c. create a django project 

    d. create an app


DJANGO PROJECT CONFIGURATION 

    a. configure the settings.py file 
    
    b. add the project app and rest_framework to the 'installed apps' object.

    c. configure the project urls.py file  
    
    d. include the project 'app urls.py' in the project urls.py file.


CRUD API PROJECT 

    a. create the api models in the models.py file
    
    b. migrate to the database using the command 'python manage.py makemigrations' 
       and 'python manage.py migrate'.

    c. create a serializers.py file in the app dir, which will be used to convert complex data types.

    d. create the logic for POST, GET, PUT AND DELETE in the views.py file.

    e. create a urls.py file in the app dir 
    
    f. create the routes using the class views created in the views.py file.


CRUD API RUN AND TESTING

    a. run the CRUD project using the command 'python manage.py runserver'.

    b. Postman App was used for testing the crud api, In testing the CRUD api;

    c. POST request is to create a new info and call the REST endpoint '/api/'.

    d. GET request is to view an info and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the     endpoint.

    e. PUT request is to update an info and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the endpoint.

    f. DELETE request is to delete an info and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the endpoint. 








