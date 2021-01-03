# Technical Documentation

## Backend

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
> (venv)$ pip install -U flask-cors

run the app

> (venv)$ app.py

app should be running on `localhost:5000` now.

#### Libraries

https://flask.palletsprojects.com/en/1.1.x/installation
https://flask-cors.readthedocs.io/en/latest/


## Frontend

#### Dependencies

- node.js
- npm

setup Vue:

> $ npm install -g @vue/cli

create new Vue project (frontend directory)

> $ cd WuePlan
> $ vue create frontend

install axios

> $ npm install axios

install bootstrap
> npm install bootstrap bootstrap-vue

start frontend server

> npm run server

app should be running on `localhost:8080` now.




#### Libraries
https://v3.vuejs.org/guide/installation.html#vue-devtools
https://www.npmjs.com/package/axios
https://bootstrap-vue.org/docs
