# Stocks Project

## Pre-Requisites

Before running this project, ensure you have the following installed and configured:

1. **Windows Subsystem for Linux (WSL)**:
   Install WSL if you haven't already:
   - [Install WSL](https://learn.microsoft.com/en-us/windows/wsl/install)

2. **Linux Distribution**:
   Choose and install your preferred Linux distribution from the Microsoft Store.

## Setup Instructions

Once you have WSL and your Linux distribution installed, follow these steps to set up and run the project:

### Install Docker

1. Update the package list:

   ```bash
   sudo apt-get update
   ```

2. Install Docker:

   ```bash
   sudo apt install docker.io
   ```

3. Start the Docker daemon:

   ```bash
   sudo dockerd
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

- **shell**: Opens a Django shell inside Docker.

   ```bash
   make shell
   ```

### Notes

- Ensure your virtual environment and project dependencies are set up as required before running Docker commands.
- Modify Dockerfile and docker-compose.yml files as necessary for your specific project configuration.
