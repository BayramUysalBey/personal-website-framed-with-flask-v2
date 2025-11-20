# Bayram Uysal's Personal Website v2.0

This is the second version of my personal website, rebuilt with modern, containerized architecture and leveraging the Neon serverless PostgreSQL database for dynamic project management.

### 🌐 Live Demo: [personal-website-framed-with-flask-v2.onrender.com](https://personal-website-framed-with-flask-v2.onrender.com/ )
### ✨ Key Features & Technical Outcomes

This project demonstrates proficiency in building and deploying a multi-component backend stack:

Full Containerization (Docker Compose): The entire application (Flask/Gunicorn) and its environment are containerized, ensuring a reliable, cross-platform build via a single command.

Externalized Secrets: All credentials (DATABASE_URL, SESSION_SECRET) are securely stored in a local .env file and never committed to the repository (a critical security practice).

Robust Deployment Pipeline: The boot.sh entrypoint includes custom Python logic for connection retries and synchronization, guaranteeing the web application starts only after the external Neon database is ready.

Neon PostgreSQL Integration: Project data is sourced from Neon, confirming experience with managed, serverless PostgreSQL and its required SSL connection settings.

Professional Server: Uses Gunicorn for production-grade web serving, moving beyond Flask's internal development server.

### 🛠 Project Stack

Backend Core: Python (3.12-slim), Flask

Production Server: Gunicorn

Database: PostgreSQL (via Neon Serverless)

Deployment: Docker, Docker Compose

### 🚀 One-Step Local Setup (The Professional Method)

To run this application locally, you only need Docker Desktop installed and running.

### Clone the Repository:

git clone [https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git](https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git)
cd personal-website-framed-with-flask-v2

### Configure Secrets:

Create a file named .env in the project root.

Add your connection URL and session secret to it (as demonstrated below).

## .env (NEVER commit this file)

### This shows the structure needed for the application

DATABASE_URL="**********"

SESSION_SECRET=**********

## Build and Launch (The Single Command):

docker compose up --build

#### The application will be available at <http://localhost:5000/>.

### 🛑 Critical Learning Outcomes (Debugging Focus)

This project served as a testbed for solving common system integration failures:

Dependency Resolution: Solved the pg_config not found error by switching from psycopg2 to the pre-compiled psycopg2-binary in requirements.txt.

Startup Synchronization: Implemented robust wait-for-database logic in boot.sh to eliminate race conditions between the application and the database service.

Security Fixes: Resolved live security incidents by removing hardcoded passwords from app.py and implementing the .gitignore/.env separation.
