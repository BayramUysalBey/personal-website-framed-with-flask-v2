from flask import Flask, render_template, jsonify

app = Flask(__name__)

PROJECTS = [{
    "project name": "Zombie Survival",
    "project content": "OOP-based zombie tracker with score system",
    "link": "https://github.com/BayramUysalBey/zombie-survival-oop"
}, {
    "project name": "Greeter App",
    "project content": "Flask greeting app with visitor counter",
    "link": "https://github.com/BayramUysalBey/flask-greeter-app"
}, {
    "project name": "Personal Website",
    "project content": "Flask personal website project",
    "link": "https://github.com/BayramUysalBey/personal-website-framed-with-flask"
}]


@app.route("/")
def hello_bayram():
    return render_template("home.html", projects=PROJECTS)


@app.route("/api/projects")
def list_projects():
    return jsonify(PROJECTS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
