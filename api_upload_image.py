import os
from tkinter import Image
from flask import Flask,jsonify,request,flash
from flask_httpauth import HTTPTokenAuth
import random
import string
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash

project_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
UPLOAD_FOLDER = 'hasil_upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
database_file = "sqlite:///{}".format(os.path.join(project_dir, "image.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file  
db = SQLAlchemy(app)
class upload(db.Model):
    image=db.Column(db.String(225),unique=False,nullable=False, primary_key=True) 

def allowed_file(filename):     
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# nama kelompok 
# rizky dwi saputra (6A) 
# moh saefudin fikri (6B) 
@app.route("/api/uploadimage", methods=["POST"])
def login_user():
    if 'image' not in request.files:
        flash('No file part')
        return jsonify({
            "pesan":"tidak ada form image"
            })
    file = request.files['image']
    if file.filename == '':
        return jsonify({
            "pesan":"tidak ada file image yang dipilih"
            })
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        path_image = upload(image=filename)
        db.session.add(path_image)
        db.session.commit()
        if db.session.commit():
            print("oke")
        return jsonify({
            "pesan":"gambar telah terupload"
            })
    else:
        return jsonify({
        "pesan":"bukan file image"
        })
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)
