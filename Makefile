# Include and export environment variables from .env file
include .env
export

# Define phony targets to avoid conflicts with file names
.PHONY: help run stop clean test cli create-db refresh-db drop-db exec-sql mysql-shell debug view restart build migrate

# Help target to display available targets and their descriptions
help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  build         to build Docker images"
	@echo "  create-db     to create MySQL database and user"
	@echo "  run           to build and run Docker containers"
	@echo "  stop          to stop Docker containers"
	@echo "  clean         to stop Docker containers and remove volumes"
	@echo "  test          to run tests inside Docker"
	@echo "  cli           to run Django CLI inside Docker"
	@echo "  refresh-db    to refresh MySQL database connection"
	@echo "  drop-db       to drop MySQL database"
	@echo "  exec-sql      to execute SQL command in MySQL"
	@echo "  mysql-shell   to access MySQL shell"
	@echo "  debug         to print environment variables"
	@echo "  view          to view Docker containers"
	@echo "  restart       to restart Docker containers"
	@echo "  migrate       to run Django migrations"

# Create MySQL database and user
create-db:
	@docker-compose exec db mysql -uroot -p${DB_ROOT_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"
	@docker-compose exec db mysql -uroot -p${DB_ROOT_PASSWORD} -e "CREATE USER IF NOT EXISTS ${DB_USER}@'%' IDENTIFIED BY '${DB_PASSWORD}';"
	@docker-compose exec db mysql -uroot -p${DB_ROOT_PASSWORD} -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO ${DB_USER}@'%';"

# Build Docker containers
build:
	@docker-compose build

# Run Docker containers
run:
	@docker-compose up

# Stop Docker containers
stop:
	@docker-compose down

# Clean up Docker containers and volumes
clean: stop
	@docker-compose down -v

# Run tests inside Docker container
test:
	@docker-compose exec web python manage.py test

# Run Django CLI inside Docker
cli:
	@docker-compose exec stocks_backend sh

# Refresh MySQL database connection
refresh-db:
	@docker-compose exec db mysqladmin -uroot -p${DB_PASSWORD} refresh

# Drop MySQL database
drop-db:
	@docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "DROP DATABASE IF EXISTS ${DB_NAME};"

# Execute SQL command in MySQL
exec-sql:
	@docker-compose exec db mysql -uroot -p${DB_ROOT_PASSWORD} -e "${SQL}"

# Access MySQL shell
mysql-shell:
	@docker-compose exec db mysql -uroot -p${DB_ROOT_PASSWORD} ${DB_NAME}

# Debug target to print environment variables
debug:
	@echo "DB_NAME: ${DB_NAME}"
	@echo "DB_USER: ${DB_USER}"
	@echo "DB_PASSWORD: ${DB_PASSWORD}"

# View Docker container status
view:
	@docker-compose ps -a

# Restart Docker containers
restart:
	@docker-compose down
	@docker-compose up --build

migrate:
	@docker-compose exec stocks_backend sh -c "cd stocks/ && python manage.py makemigrations && python manage.py migrate"