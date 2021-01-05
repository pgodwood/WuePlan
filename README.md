// markdown cheatsheet https://res.cloudinary.com/practicaldev/image/fetch/s--2rTn_7XO--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://dev-to-uploads.s3.amazonaws.com/i/5zhubbpov3m3ly9a1t9c.png

# Technical Documentation

## Backend

#### Structure

| name      | description                                                            |
|-----------|------------------------------------------------------------------------|
| app.py    | REST API endpoints consuming and producing JSON requests and responses |
| config.py | configurations settings for Flask app                                  |
| models.py | define classes that are used for the app                               |
| exams.py  | algorithm for calculating the exam plan                                |

#### Dependencies

- python
- pip

setup backend:

> $ mkdir backend
> $ cd backend

install virtual environment:

> $ python -m venv venv`

activate virtual environment. to deactivate, just `(venv)$ deactivate`

> $ cd venv\scripts
> $ activate

install flask

> (venv)$ pip install flask
> (venv)$ pip install flask-cors

install db

> (venv)$ pip install flask-sqlalchemy

run the app

> (venv)$ app.py

save the requirements:

> pip freeze > requirements.txt

app should be running on `localhost:5000` now.

#### API
All API Endpoints should be listed here.
// take a look at swagger to have it created automatically
// https://kanoki.org/2020/07/18/python-api-documentation-using-flask-swagger/
// https://editor.swagger.io/#/   -> so soll es ausschauen
// https://dev.to/djiit/documenting-your-flask-powered-api-like-a-boss-9eo

#### Libraries

https://flask.palletsprojects.com/en/1.1.x/installation
https://flask-cors.readthedocs.io/en/latest/


## Frontend

#### Structure

| name       | explanation                                                                     |
|------------|---------------------------------------------------------------------------------|
| main.js    | app entry point. loads & initializes Vue with the root component                |
| App.vue    | root component. starting point from which all other components will be rendered |
| router.js  | define URLs and map them to components                                          |
| views      | all UI components tied to the router are stored here                            |
| components | all UI components are stored here                                               |
| assets     | stattic assets (e.g. images or fonts) are stored here                           |

#### Dependencies

- node.js
- npm

setup Vue:

> $ npm install -g @vue/cli

create new Vue project (frontend directory)

> $ cd WuePlan
> $ vue create frontend
> $ cd frontend

install axios

> $ npm install axios --save

install bootstrap
> npm install bootstrap bootstrap-vue
or (test first):
> $ vue create bootstrap-vue-app
> $ cd create bootstrap-vue-app
> $ vue add bootstrap-vue

start frontend server

> npm run server

app should be running on `localhost:8080` now.

#### Libraries
https://v3.vuejs.org/guide/installation.html#vue-devtools
https://www.npmjs.com/package/axios
https://bootstrap-vue.org/docs

## Docker

#### Installation

#### Libraries
https://kr.vuejs.org/v2/cookbook/dockerize-vuejs-app.html



## Notes

code library:
https://www.codegrepper.com/code-examples/javascript/send+csv+file+from+axios+to+flask

tutorial considering all tools & tests!
https://github.com/mjhea0/flaskr-tdd

HTML & bootstrap low-code generator
https://bootsnipp.com/forms

**good general library**
https://www.w3schools.com/howto/howto_js_collapse_sidebar.asp

Tutorial Flask Upload file
https://www.tutorialspoint.com/flask/flask_file_uploading.htm

Webpack vs npm run build
https://stackoverflow.com/questions/46214132/how-can-i-combine-vue-js-with-flask

nice considerations what Webapp tool to use (python):
https://amontalenti.com/2012/06/14/web-app

**ToDo:**
Webserver: WSGI deployment: https://flask.palletsprojects.com/en/1.1.x/deploying/
Database: Flask-SQL-Alchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
App.CONFIG file

extensive tutorial:
https://stackabuse.com/single-page-apps-with-vue-js-and-flask-restful-api-with-flask/

nice documentation & input:
https://libraries.io/github/frol/flask-restplus-server-example
