# socialmediaprojectassignments

Based on Python 3.11

# Install Python version 3.11 according to the operation system
# Getting Started:
# create image for this project using the command
$ docker build -t django_assignment .

# run docker container
$ docker run -p 8000:8000 django_assignment 

# create dummy superuser

$ docker ps
$ docker exec -it container_name python manage.py create_dumpy_superuser

after running above command super user created with email="admin@example.com" and password="pass1234"




