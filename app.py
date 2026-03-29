import os
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, jsonify, redirect
from database import load_projects_from_db, load_project_from_db_by_id, SessionLocal, Project

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


@app.route("/project/<int:id>")
def show_project(id):    
    project = load_project_from_db_by_id(id)
    
    if project:
        return render_template("projectpage.html", project=project)
    else:
        print(f"DEBUG: Project with ID {id} not found for API.")
        return jsonify({"error": "Project not found"}), 404

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
    app.debug = True
    app.run(host='0.0.0.0', port=5000, debug=True)
