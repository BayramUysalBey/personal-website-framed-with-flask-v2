# Bayram Uysal's Personal Website v2.0  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg )](LICENSE)  

> This is the second version of my personal website, rebuilt with PostgreSQL (via Neon) for dynamic project management.  
> Live demo: [https://personal-website-framed-with-flask-v2.onrender.com/ ](https://personal-website-framed-with-flask-v2.onrender.com/ )  

![App Screenshot](static/flask_web_1.png)  
![App Screenshot](static/flask_web_2.png)  

## ✨ Key Features & Enhancements  
* **Dynamic Content**: Project data is fetched from **PostgreSQL (Neon)**, enabling real-time updates without code changes.  
* **CRUD Functionality**: Backend supports **Create, Read, Update, and Delete** operations for projects (critical for junior backend roles).  
* **Contact Form**: Collects user messages (backend logic in development).  
* **Database Logging**: Tracks project interactions in PostgreSQL.  
* **Deployed to Render**: Cloud-hosted for 24/7 availability.  

## 🛠 Built With  
* **Python/Flask**: Core web framework.  
* **PostgreSQL (Neon)**: Relational database for scalable backend logic.  
* **SQLAlchemy**: ORM for database interactions.  
* **HTML/CSS/Bootstrap**: Frontend design and styling.  
* **Git/GitHub**: Version control and collaboration.  
* **Render**: Deployment and hosting platform.  

## 🚀 Run Locally  
1. Ensure Python is installed.  
2. Clone the repository:  
```bash  
git clone https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git


Navigate to the project directory:
bash


1
cd personal-website-framed-with-flask-v2  
Create and activate a virtual environment:
bash


1
2
3
python -m venv venv  
# Windows: venv\Scripts\activate  
# macOS/Linux: source venv/bin/activate  
Install PostgreSQL dependencies:
bash


1
pip install -r requirements-neon.txt  
Configure Neon Database:
Create a Neon project and copy the connection string (e.g., postgres://user:password@ep-cool-dark-842271.us-east-2.aws.neon.tech/neondb).
Add to .env:
env


1
DATABASE_URL="postgres://user:password@ep-cool-dark-842271.us-east-2.aws.neon.tech/neondb?sslmode=require"  
Run the app:
bash


1
flask run  
📋 Neon-Specific Fixes
A. Database Schema Adjustments
PostgreSQL requires explicit type casting. Update your models to match Neon’s schema:

python


1
2
3
4
5
6
7
8
⌄
# models.py  
class Project(db.Model):  
    __tablename__ = 'projects'  
    id = db.Column(db.Integer, primary_key=True)  # PostgreSQL uses SERIAL for auto-increment  
    project_name = db.Column(db.String(250), nullable=False)  
    content = db.Column(db.String(250), nullable=False)  
    link = db.Column(db.String(250), nullable=True)  
    languages = db.Column(db.String(2000), nullable=True)  
B. Neon Connection String
Neon’s format:

python


1
2
db_connection_string = "postgres://user:password@ep-cool-dark-842271.us-east-2.aws.neon.tech/neondb?sslmode=require"  
engine = create_engine(db_connection_string, connect_args={"sslmode": "require"})  
C. Requirements Update
Replace mysqlclient with PostgreSQL drivers in requirements-neon.txt:

txt


1
2
3
4
Flask  
Flask-SQLAlchemy  
psycopg2-binary  # For local development  
gunicorn  
🌐 Neon Deployment Notes
SSL Mode : Neon enforces sslmode=require. Ensure your connect_args include:
python


1
connect_args={"sslmode": "require"}  
Schema Differences :
MySQL’s auto_increment → PostgreSQL’s SERIAL (handled via db.Column(db.Integer, primary_key=True) in SQLAlchemy).
🧠 Learning Outcomes
Successfully migrated from MySQL to Neon PostgreSQL.
Mastered SQLAlchemy quirks with PostgreSQL (e.g., SERIAL vs. auto_increment).
Configured Neon’s SSL requirements for secure connections.
🛑 Critical Warnings
Neon Free Tier : Connections drop after inactivity. Use keepalive or a background worker to maintain uptime.
PostgreSQL Syntax : Ensure all queries use PostgreSQL dialect (e.g., ILIKE instead of LIKE).
