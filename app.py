from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [{
    "id": 1,
    "project name": "Zombie-Survival (OOP)",
    "project content": "Word-based simulator game based on Python-OOP"
}, {
    "id":
    2,
    "project name":
    "Greeter-App (Flask)",
    "project content":
    "Greetings website built using the Flask framework"
}, {
    "id": 3,
    "project name": "Personal Website (Flask)",
    "project content": "In progress"
}]


@app.route("/")
def hello_bayram():
    return render_template("home.html", projects=PROJECTS)


@app.route("/api/projects")
def list_projects():
    return jsonify(PROJECTS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
