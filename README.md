# Stock Prediction Project

## Pre-Requisites

Before running this project, ensure you have the following installed and configured:

1. **Windows Subsystem for Linux (WSL)**:
   Install WSL if you haven't already:
   - [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

2. **Linux Distribution**:
   Choose and install your preferred Linux distribution from the Microsoft Store.

## Setup Instructions

Once you have WSL and your Linux distribution installed, follow these steps to set up and run the project:

### MySQL Setup

#### 1. Installing MySQL

Ensure your WSL environment is updated and ready for installation:

```bash
sudo apt update
sudo apt upgrade
```

Install MySQL Server:

```bash
sudo apt install mysql-server
```

During the installation process, you may be prompted to set a root password for MySQL. If not, proceed to the next step.

#### 2. Configuring MySQL

MySQL on WSL uses `auth_socket` authentication by default for the `root` user, allowing you to log in without a password if you are logged in as the Unix `root` user.

##### Accessing MySQL as Root User (Using `auth_socket` Authentication)

1. **Login as Unix Root User:**

   Start by switching to the Unix `root` user:
   ```bash
   sudo su -
   ```

2. **Access MySQL as Root:**

   Once you are the Unix `root` user, access MySQL without a password:
   ```bash
   mysql -u root
   ```

3. **Set a Password for the MySQL Root User (Optional):**

   If you prefer to use password-based authentication for the `root` user:
   ```sql
   ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password';
   FLUSH PRIVILEGES;
   ```

   Replace `'your_password'` with your desired password.

4. **Exit MySQL and Unix Root User:**

   Exit the MySQL prompt and then exit from the Unix `root` user mode:
   ```sql
   exit;
   exit;
   ```

5. **Login to MySQL with Password (If Password Set):**

   If you set a password for the `root` user, login to MySQL using:
   ```bash
   mysql -u root -p
   ```

   Enter the password when prompted.

##### Accessing MySQL with `sudo`

Alternatively, you can use `sudo` to access MySQL as the `root` user without switching to the Unix `root` mode:

```bash
sudo mysql
```

This will prompt for your user password and allow you to access MySQL as the `root` user.

### Docker Setup

1. Update the package list:

   ```bash
   sudo apt-get update
   ```

2. Install Docker and Docker Compose:

   ```bash
   sudo apt install docker.io
   sudo apt install docker-compose
   ```

3. Start the Docker daemon:

   ```bash
   sudo dockerd
   ```

### Setting up Environment Variables

Create a `.env` file in your project directory and add the following variables:

```bash
DB_NAME=<db-name>
DB_USER=root
DB_PASSWORD=<db-password>
DB_HOST=localhost
DB_PORT=3306
```

### How to Run This Project

To run this project, use the following commands in your Linux terminal:

- **help**: Displays a brief description of available targets.

   ```bash
   make help
   ```

- **run**: Builds and starts Docker containers.

   ```bash
   make run
   ```

- **stop**: Stops Docker containers.

   ```bash
   make stop
   ```

- **clean**: Stops Docker containers and removes volumes.

   ```bash
   make clean
   ```

- **test**: Executes Django tests inside Docker.

   ```bash
   make test
   ```

- **cli**: Opens a Django shell inside Docker.

   ```bash
   make cli
   ```

- **setup-db**: Sets up MySQL server using Docker Compose.

   ```bash
   make setup-db
   ```

- **create-db**: Creates MySQL database and user.

   ```bash
   make create-db
   ```

- **refresh-db**: Refreshes MySQL database connection.

   ```bash
   make refresh-db
   ```

- **drop-db**: Drops MySQL database.

   ```bash
   make drop-db
   ```

- **exec-sql**: Executes SQL command in MySQL.

   ```bash
   make exec-sql SQL="YOUR_SQL_COMMAND_HERE"
   ```

- **mysql-shell**: Accesses MySQL shell.

   ```bash
   make mysql-shell
   ```

### Notes

- Ensure your virtual environment and project dependencies are set up as required before running Docker commands.
- Modify Dockerfile and docker-compose.yml files as necessary for your specific project configuration.
