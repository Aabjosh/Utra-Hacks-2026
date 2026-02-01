from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import pathSegmenter

app = Flask(__name__)

BASE_DIR = os.path.dirname(__file__)
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

def allowed_file(filename):
    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        imageFile = request.files.get("image")

        if not imageFile or imageFile.filename == "":
            return "No image uploaded", 400

        if not allowed_file(imageFile.filename):
            return "Invalid file type", 400

        imageBytes = imageFile.read()

        pathSegmenter.runImageProcessor(imageBytes)

        imageFile.stream.seek(0)

        filename = secure_filename(imageFile.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        imageFile.save(save_path)

        return f"Image processed and saved to: {save_path}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
