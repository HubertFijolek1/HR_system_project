# --- Stage 1: Build ---
    FROM python:3.9-slim AS build

    # Prevent Python from writing pyc files and enable unbuffered output
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    WORKDIR /app
    
    # Install system dependencies
    RUN apt-get update && apt-get install -y \
        gcc \
        libpq-dev \
        build-essential \
     && rm -rf /var/lib/apt/lists/*
    
    # Install Python dependencies into /install
    COPY requirements.txt /app/
    RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt
    
    # Copy project code
    COPY . /app/
    
    # --- Stage 2: Final ---
    FROM python:3.9-slim
    ENV PYTHONDONTWRITEBYTECODE 1
    ENV PYTHONUNBUFFERED 1
    
    WORKDIR /app
    
    # Copy dependencies from build stage
    COPY --from=build /install /usr/local
    COPY . /app/
    
    EXPOSE 8000
    CMD ["gunicorn", "hr_system.wsgi:application", "--bind", "0.0.0.0:8000"]
    