# Makefile for Dockerized Django Project

# Variables
DOCKER_COMPOSE = docker-compose

.PHONY: help run stop clean test cli

help:
	@echo Please use 'make <target>' where <target> is one of:
	@echo "  run         to build and run Docker containers"
	@echo "  stop        to stop Docker containers"
	@echo "  clean       to stop Docker containers and remove volumes"
	@echo "  test        to run tests inside Docker"
	@echo "  cli         to run Django CLI inside Docker"

# Build and run the Docker containers
run:
	$(DOCKER_COMPOSE) up --build

# Stop the Docker containers
stop:
	$(DOCKER_COMPOSE) down

# Stop Docker containers and remove volumes
clean: stop
	$(DOCKER_COMPOSE) down -v

# Run tests inside the Docker container
test:
	$(DOCKER_COMPOSE) exec web python manage.py test

# Run Django CLI inside the Docker container
cli:
	$(DOCKER_COMPOSE) exec web python manage.py shell
