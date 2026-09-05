from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, BigInteger

import os

database_url = os.environ.get("DATABASE_URL")


if not database_url:
    raise ValueError(
        "DATABASE_URL environment variable is not set. Please set it for your database connection."
    )

engine = create_engine(database_url)

Base = declarative_base()


class Project(Base):
    __tablename__ = 'projects'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    project_name = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)
    link = Column(String(250))
    languages = Column(String(200))
    live_link = Column(String(250), nullable=True)

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
    db_session = SessionLocal()
    try:
        project = db_session.query(Project).get(project_id)

        if project:
            return {
                'id': project.id,
                'project_name': project.project_name,
                'content': project.content,
                'link': project.link,
                'languages': project.languages,
                'live_link': project.live_link
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
