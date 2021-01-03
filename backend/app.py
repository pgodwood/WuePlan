import os
import sqlite3
#import pandas as pd #pip install pandas
#from sqlalchemy import create_engine
from flask import Flask
from flask import render_template
from flask import request, url_for, flash, redirect
from flask import jsonify
from flask_cors import CORS
from random import * # für Testrouting
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row #have name-based access to columns
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

# SQL Alchemy
#def connect_db():
#    engine = create_engine('database.db')
#    return engine

# Excel in dataFrame umschreiben
#def get_excel(path):
#    file = pd.read_excel(path)
#    df = pd.DataFrame(file)
#    flash("""File erkannt...\n
#    Beginne mit Upload in DatenBank.""")

#    connect_db()
#    file.to_sql(name=exams,con =engine,if_exists='replace')


app = Flask(__name__,
            static_folder = "../dist/static", # Verweis auf build server Pfad von FE
            template_folder = "../dist")
CORS(app)
app.config['SECRET_KEY'] = 'ichbineinganzlangerundsichererstring123456'

#cors = CORS(app, resources={r"/*": {"origins"; "*"}}) # Flask-backend direkt vom FE aufrufen

#app.config['DEBUG'] = True # Debug Modus um Änderungen ohne Server-Neustart zu machen -> umgangen mit $python app.py





#
#Infos über config file:
#https://pythonise.com/series/learning-flask/flask-configuration-files
#

################################
#### Übergabe an vue-router ####
################################
# Flask gibt routing jetzt immer an vue.router über
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

# ALTE Startseite mit Flask & JINJA
#@app.route('/startseite')
#def index():
#    conn = get_db_connection()
#    posts = conn.execute('SELECT * FROM posts').fetchall() #select all entries from post table and get all rows from the query
#    conn.close()
#    return render_template('index.html', posts=posts)

#####################
### TEST-Endpoint ###
#####################

@app.route('/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100),
        'test': "test"
    }
    return jsonify(response)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))

@app.route('/upload')
def upload():
   return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'Datei erfolgreich hochgeladen'

# run with (venv)$ python app.py
if __name__ == '__main__':
   app.run(debug = True)
