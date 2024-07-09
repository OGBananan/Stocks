#Setup the enviorment variables
include .env
export

# Targets
.PHONY: help setup-db run stop clean test cli create-db refresh-db \
        drop-db exec-sql mysql-shell

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  run           to build and run Docker containers"
	@echo "  stop          to stop Docker containers"
	@echo "  clean         to stop Docker containers and remove volumes"
	@echo "  test          to run tests inside Docker"
	@echo "  cli           to run Django CLI inside Docker"
	@echo "  setup-db      to setup MySQL server"
	@echo "  create-db     to create MySQL database and user"
	@echo "  refresh-db    to refresh MySQL database connection"
	@echo "  drop-db       to drop MySQL database"
	@echo "  exec-sql      to execute SQL command in MySQL"
	@echo "  mysql-shell   to access MySQL shell"

# Setup MySQL server using Docker Compose
setup-db:
	docker-compose up -d db

# Build and run the Docker containers
run:
	docker-compose up

# Stop the Docker containers
stop:
	docker-compose down

# Stop Docker containers and remove volumes
clean: stop
	docker-compose down -v

# Run tests inside the Docker container
test:
	docker-compose exec web python manage.py test

# Run Django CLI inside the Docker container
cli:
	docker-compose exec web python manage.py shell

# Create MySQL database and user
create-db:
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "CREATE DATABASE IF NOT EXISTS ${DB_NAME};"
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "CREATE USER IF NOT EXISTS '${DB_USER}'@'%' IDENTIFIED BY '${DB_PASSWORD}';"
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "GRANT ALL PRIVILEGES ON ${DB_NAME}.* TO '${DB_USER}'@'%';"

# Refresh MySQL database connection
refresh-db:
	docker-compose exec db mysqladmin -uroot -p${DB_PASSWORD} refresh

# Drop MySQL database
drop-db:
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "DROP DATABASE IF EXISTS ${DB_NAME};"

# Execute SQL command in MySQL
exec-sql:
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} -e "${SQL}"

# Access MySQL shell
mysql-shell:
	docker-compose exec db mysql -uroot -p${DB_PASSWORD} ${DB_NAME}
