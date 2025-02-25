## Overview
This internal HR system is built using Django for the backend, PostgreSQL for the database, and Docker for containerization. It is designed to support recruitment, time tracking, leave management, and employee evaluations.

## Components
- **Web Service:** Runs the Django application via Gunicorn.
- **Database Service:** PostgreSQL container storing HR data.
- **CI/CD:** To be configured via GitHub Actions.

## Deployment
- **Docker Compose** orchestrates both the web and database services.
- The system is deployed on a Linux (Ubuntu) environment.