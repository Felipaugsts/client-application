# Makefile for Django App

# Define variables
PYTHON = python
DJANGO_MANAGE = python AuthClient/manage.py

# Run the development server
run:
	cd ./gateway
	$(DJANGO_MANAGE) runserver

# Create a new Django superuser
createsuperuser:
	cd ./gateway
	$(DJANGO_MANAGE) createsuperuser

# Run database migrations
migrate:
	cd ./gateway
	$(DJANGO_MANAGE) makemigrations
	$(DJANGO_MANAGE) migrate

.PHONY: run createsuperuser migrate createapp test rungateway cleanpyc