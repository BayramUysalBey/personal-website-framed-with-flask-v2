# Bayram Uysal's personal website v2.0  
[!  [License: MIT] (https://img.shields.io/badge/licence-mit-green.svg)] (undergraduate)  

> This is the second version of the personal website that has been rebuilt by postgresql (through neon) for dynamic project management.  
> Live demo: [personal-website-filed-with-fask-v2.onrender.com] (https://personal-website-with-with-flask-v2.onrender.com/)  

!  [Application screenshot] (static/flask_web_1.png)  
!  [Application screenshot] (static/flask_web_2.png)  

## ✨ Basic features and improvements  
- ** Dynamic Content **: Project data ** Postgresql (Neon) ** is taken from ** and activates real -time updates without code changes.  
- ** CUD Functionality **: Rear end support ** Create, read, update and delete operations (critical for Junior Back end roles).  
- ** Contact Form **: Collects user messages (rear end logic on the development back).  
- ** Database Diary **: Monitoring project interactions in Postgresql.  
- ** distributed for render **: 7/24 Cloud for availability.  

## 🛠  
- ** Python/Flask **: Core Web Framework.  
- ** Postgresql (Neon) **: Relational database for scalable rear end logic.  
- ** sqlalchemy **: ORM for database interactions.  
- ** HTML/CSS/Bootstrap **: front end design and style.  
- ** Go/github **: version control and cooperation.  
- ** Render **: Distribution and Host Platform.  

## 🚀 Run locally  
1. Make sure that Python was established.  
2. Clon the tank:  
   `` Bash  
   Go clone https://github.com/bayramusalbey/personal-website-with-flask-v2.git
3. Go to the project directory:
   `` Bash
   CD Personal-Website-Freed-With-Fask-V2
4. Create and activate a virtual environment:
   `` Bash
   Python -m Venv Venv  
   # Windows: Venv \ Scripts \ Activate  
   # MacOS/Linux: Source Venv/Bin/Activity
5. Upload postgresql addictions:
   `` Bash
   PIP Installation -r requirements -Non.txt
6. Configure the Neon database:
-Create a neon project and copy the connection string (eg [postgres://user:password@ep-cool-dark-842271.us-east-2.aws.neon.tech/neondb]).
-Add to [.env]:
`` env
DATABASE_URL="postgres://user:password@ep-cool-dark-842271.us-east-2.aws.neon.tech/neondb?sslmode=require"
7. Run the app:
   `` Bash
   flask run
   
