# coding=utf-8

import os
from flask import Flask, request, render_template, jsonify
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/upload_file/", methods=['POST'])
def upload_file():
    upload_status = True
    files = request.files
    if files != '':
        for key, file_obj in files.items():
            file_name = secure_filename(files[key].filename)
            file_obj.save(os.path.join("./docxs", file_name))
    else:
        upload_status = False 
    result = {
        'res': upload_status 
    }
    return jsonify(result)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=8089)
