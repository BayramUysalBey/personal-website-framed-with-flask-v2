from flask import Flask, render_template, jsonify, redirect
from database import load_projects_from_db, SessionLocal, Project

app = Flask(__name__)


@app.route("/")
def home():
    projects = load_projects_from_db()
    print(f"DEBUG (app.py): Projects loaded for template: {projects}")
    return render_template("home.html", projects=projects)


@app.route("/api/projects")
def list_projects():
    projects = load_projects_from_db()
    return jsonify(projects)

@app.route('/project/<int:id>/delete', methods=['POST'])  
def delete_project(id):
    db_session = SessionLocal()
    try:
        project_to_delete = db_session.query(Project).get(id)
        if project_to_delete:
            db_session.delete(project_to_delete)
            db_session.commit()
            print(f"DEBUG: Project with ID {id} successfully deleted.")
        else:
            print(f"DEBUG: Project with ID {id} not found for deletion.")
    except Exception as e:
        db_session.rollback()
        print(f"ERROR: Failed to delete project with ID {id}. Error: {e}")
    finally:
        db_session.close()
    return redirect('/')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
