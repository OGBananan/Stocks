# Dockerfile
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /stocks

# Install dependencies
COPY requirements.txt /stocks/
RUN pip install -r requirements.txt

# Copy project
COPY . /stocks/

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
