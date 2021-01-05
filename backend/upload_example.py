def uploadAudio():

    def is_allowed(filename):
        return len(filter(lambda ext: ext in filename, ["wav", "mp3", "ogg"])) > 0

    file = request.files.getlist("audio")[0]

    if file and is_allowed(file.filename):
        filename = secure_filename(file.filename)
        file_path = path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # convert_to_mono_wav(file_path, True)

        response = jsonify(get_prediction(file_path))
    else:
        response = bad_request("Invalid file")

    return response

#############################################

# https://pythonise.com/series/learning-flask/flask-uploading-files

###########################################

# now: https://riptutorial.com/flask/example/19418/save-uploads-on-the-server

import os
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename

# Create a directory in a known location to save files to.
uploads_dir = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads_dir, exists_ok=True)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # save the single "profile" file
        profile = request.files['profile']
        profile.save(os.path.join(uploads_dir, secure_filename(profile.filename)))

        # save each "charts" file
        for file in request.files.getlist('charts'):
            file.save(os.path.join(uploads_dir, secure_filename(file.name)))

        return redirect(url_for('upload'))

    return render_template('upload.html')
