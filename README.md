# Bayram Uysal's Personal Website v2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

This is the second version of my personal website, built with a robust backend to showcase my projects dynamically.

You can view the live demo here: **[https://personal-website-framed-with-flask-v2.onrender.com/](https://personal-website-framed-with-flask-v2.onrender.com/)**

![App Screenshot](static/flask_web_1.png) 
![App Screenshot](static/flask_web_2.png)

## ✨ Key Features & Enhancements
* **Dynamic Content:** Project data is now fetched from a **MySQL database**, allowing for easy updates without changing the code.
* **CRUD Functionality:** The backend supports **Create, Read, Update, and Delete** operations for managing projects (a key skill for backend developers!).
* **Contact Form:** A form where visitors can send me questions or messages (backend logic in development).
* **Database Logging:** All actions are logged in the database.
* **Deployed to Render:** The application is deployed on a cloud platform for 24/7 availability.

## 🛠 Built With

* **Python/Flask:** The core web framework.
* **MySQL:** A relational database used for storing project data.
* **SQLAlchemy:** An Object-Relational Mapper (ORM) for interacting with the database.
* **HTML/CSS/Bootstrap:** Frontend design and styling.
* **Git/GitHub:** Version control and collaboration.
* **Render:** Continuous deployment and hosting.

## 🚀 Run Locally

1.  Make sure you have Python installed.
2.  Clone the repository:
    ```bash
    git clone [https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git](https://github.com/BayramUysalBey/personal-website-framed-with-flask-v2.git)
    ```
3.  Navigate to the project directory:
    ```bash
    cd personal-website-framed-with-flask-v2
    ```
4.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
5.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6.  **Configure your database connection:**
    Create a `.env` file in the root directory and add your database connection URL.
    **Example:**
    ```
    DATABASE_URL="mysql+pymysql://<user>:<password>@<host>/<database_name>"
    ```
7.  Run the Flask app:
    ```bash
    flask run
    ```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and submit a pull request.
