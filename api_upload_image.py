from flask import Flask, jsonify,request,flash,redirect
from itsdangerous import json
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
UPLOAD_FOLDER = 'hasil_upload'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):     
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.route("/api/uploadimage", methods=["POST"])
def index():
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
    return jsonify({
          "pesan":"gambar telah terupload"
        })
  else:
    return jsonify({
      "pesan":"bukan file image"
    })

if __name__ == '__main__':
  app.run(debug = True, port=4000)