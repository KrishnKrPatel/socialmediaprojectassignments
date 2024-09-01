# socialmediaprojectassignments

IDI Project Backend
Based on Python 3.11

Install Python version 3.11 according to the operation system
Install Postgres version 15.5 and PGAdmin to interact with the database
Getting Started
Setup project environment using venv.

Environment Variables
Create .env file in the root and add following parameters with the values
DB_NAME= 'DB_NAME'
DB_USER= 'DB_USER'
DB_PASSWORD= 'DB_PASSWORD'
DB_HOST= 'DB_HOST'
DB_PORT= 'DB_PORT'
DEBUG= ''
SECRET_KEY= ''

bash

$ python -m venv project-env
$ project-env/bin/activate
$ pip install -r requirements.txt
 
 
# Run migrations and start server
$ cd IDI_PROJECT_ROOT/
$ python manage.py migrate
$ python manage.py runserver

For more visit:
Python Docs
Django Docs
Django Rest Framework Docs
Postgres
