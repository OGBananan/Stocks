# Dockerfile
FROM python:3.10.12

# Install dependencies
COPY requirements.txt /stocks/
RUN pip install --no-cache-dir -r requirements.txt



# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Mounts the application code to the image
COPY . code
WORKDIR /code

# Run the Django development server
CMD ["python", "stocks/manage.py", "runserver", "0.0.0.0:8000"]
