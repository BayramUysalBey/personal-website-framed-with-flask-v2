from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

import os
import pymysql

db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

print(f"DEBUG: DB_USERNAME from env: '{db_username}'")
print(f"DEBUG: DB_PASSWORD from env: '{db_password}'")
print(f"DEBUG: DB_HOST from env: '{db_host}'")
print(f"DEBUG: DB_NAME from env: '{db_name}'")

if not all([db_username, db_password, db_host, db_name]):
    raise ValueError(
        "One or more database environment variables (DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME) are not set. Please check Replit Secrets."
    )

db_connection_string = f"mysql+pymysql://{db_username}:{db_password}@{db_host}/{db_name}?charset=utf8mb4"

print(f"DEBUG: Attempting to parse URL: '{db_connection_string}'")

if not db_connection_string:
    raise ValueError(
        "DB_CONNECTION_STRING environment variable is not set. Please check Replit Secrets."
    )

ca_certificate_path = "cacert-2025-05-20.pem"

engine = create_engine(
    os.environ.get("DB_CONNECTION_STRING"),
    connect_args={"ssl": {
        "ca": ca_certificate_path
    }}
)

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    image_url = Column(String(255))
    github_url = Column(String(255))      

    def __repr__(self):
        return f"<Project(id={self.id}, name='{self.project_name}', languages='{self.languages}')>"


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_projects_from_db():
    projects = []
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM projects"))
        column_names = result.keys()
        for row in result.all():
            projects.append(dict(zip(column_names, row)))
    return projects

def load_project_from_db_by_id(project_id):
    """Loads a single project from the database by its ID."""
    db_session = SessionLocal()
    try:
        project = db_session.query(Project).get(project_id)
        
        if project:
            return {
                'id': project.id,
                'title': project.title,
                'description': project.description,
                'image_url': project.image_url,
                'github_url': project.github_url
            }
        return None 
    finally:
        db_session.close()

    
if __name__ == "__main__":
    print("Attempting to load projects for debugging...")
    my_projects = load_projects_from_db()
    if my_projects:
        print("Projects loaded successfully (from database.py directly):")
        for project in my_projects:
            print(project)
    else:
        print("No projects loaded or an error occurred during direct test.")