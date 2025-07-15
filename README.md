# Bayram Uysal's Personal Website v2.0  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg )](LICENSE)  

> This is the second version of my personal website, rebuilt with PostgreSQL (via Neon) for dynamic project management.  
> Live demo: [personal-website-framed-with-flask-v2.onrender.com](https://personal-website-framed-with-flask-v2.onrender.com/ )  

![App Screenshot](static/flask_web_1.png)  
![App Screenshot](static/flask_web_2.png)  

## ✨ Key Features & Enhancements  
- **Dynamic Content**: Project data is fetched from **PostgreSQL (Neon)**, enabling real-time updates without code changes.  
- **CRUD Functionality**: Backend supports **Create, Read, Update, and Delete** operations for projects (critical for junior backend roles).  
- **Contact Form**: Collects user messages (backend logic in development).  
- **Database Logging**: Tracks project interactions in PostgreSQL.  
- **Deployed to Render**: Cloud-hosted for 24/7 availability.  

## 🛠 Built With  
- **Python/Flask**: Core web framework.  
- **PostgreSQL (Neon)**: Relational database for scalable backend logic.  
- **SQLAlchemy**: ORM for database interactions.  
- **HTML/CSS/Bootstrap**: Frontend design and styling.  
- **Git/GitHub**: Version control and collaboration.  
- **Render**: Deployment and hosting platform.  

## 🚀 Run Locally  
1. Ensure Python is installed.  
2. Clone the repository:  
   ```bash  
   git clone https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git
3. Navigate to the project directory:
   ```bash
   cd personal-website-framed-with-flask-v2
4. Create and activate a virtual environment:
   ```bash
   python -m venv venv  
   # Windows: venv\Scripts\activate  
   # macOS/Linux: source venv/bin/activate
5. Install PostgreSQL dependencies:
   ```bash
   pip install -r requirements-neon.txt
6. Configure Neon Database:
   
