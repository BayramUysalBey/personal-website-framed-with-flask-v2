import os
from sqlalchemy import create_engine, text

db_username = os.environ.get("DB_USERNAME")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_name = os.environ.get("DB_NAME")

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

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ca": ca_certificate_path
                       }})


def load_projects_from_db():
    try:
        with engine.connect() as conn:

            tables_result = conn.execute(text("SHOW TABLES"))

            visible_tables = [row[0] for row in tables_result.fetchall()]
            print(
                f"DEBUG: Tables visible to this connection: {visible_tables}")

            result = conn.execute(text("SELECT * FROM projects"))
            projects = [dict(row) for row in result.mappings()]
            print(f"DEBUG: Result from SELECT * FROM projects: {projects}")
            print(f"DEBUG: Found {len(projects)} projects.")
            return projects
    except Exception as e:
        print(f"Database Connection/Query Error: {e}")
        return []


if __name__ == "__main__":
    print("Attempting to load projects for debugging...")
    my_projects = load_projects_from_db()
    if my_projects:
        print("Projects loaded successfully (from database.py directly):")
        for project in my_projects:
            print(project)
    else:
        print("No projects loaded or an error occurred during direct test.")
