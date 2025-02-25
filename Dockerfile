# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Prevent Python from writing pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project code
COPY . /app/

# Expose port 8000 and run gunicorn server
EXPOSE 8000
CMD ["gunicorn", "hr_system.wsgi:application", "--bind", "0.0.0.0:8000"]