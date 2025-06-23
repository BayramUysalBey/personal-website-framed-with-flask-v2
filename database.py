from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://o0ebmxqjasajdcqk8nkt:pscale_pw_GOxfcW7og4Iy9n7tHRLVCO6faQMPhG5dMVmG0gmBuVX@aws.connect.psdb.cloud/personal-website-framed-with-flask?charset=utf8mb4"

# Ensure this path is correct as verified with MySQL Workbench
ca_certificate_path = "cacert-2025-05-20.pem" # Or your absolute path, if needed

engine = create_engine(db_connection_string,
                       connect_args={
                           "ssl": {
                               "ca": ca_certificate_path
                           }
                       })

def load_projects_from_db():
    try:
        with engine.connect() as conn:
            # First, list all tables to confirm connection and visible tables
            tables_result = conn.execute(text("SHOW TABLES"))
            # Make sure to fetch all results from the SHOW TABLES query
            visible_tables = [row[0] for row in tables_result.fetchall()]
            print(f"DEBUG: Tables visible to this connection: {visible_tables}")

            # Now, try to query the projects table
            result = conn.execute(text("SELECT * FROM projects"))
            projects = [dict(row) for row in result.mappings()]

            print(f"DEBUG: Result from SELECT * FROM projects: {projects}")
            if not projects:
                print("DEBUG: No projects returned from the 'projects' table (even though it might be visible).")
            else:
                print(f"DEBUG: Found {len(projects)} projects.")

            return projects
    except Exception as e:
        print(f"Database Connection/Query Error: {e}")
        return []

# No need to include app.run here, this is for debugging the function
if __name__ == "__main__":
    print("Attempting to load projects for debugging...")
    my_projects = load_projects_from_db()
    if my_projects:
        print("Projects loaded successfully (from database.py directly):")
        for project in my_projects:
            print(project)
    else:
        print("No projects loaded or an error occurred during direct test.")