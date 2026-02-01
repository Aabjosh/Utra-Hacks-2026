# app.py
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Make sure this folder exists on your PC
OUTPUT_FOLDER = os.path.join(os.getcwd(), "output_files")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")

        # Generate a text file
        file_path = os.path.join(OUTPUT_FOLDER, f"{name}_info.txt")
        with open(file_path, "w") as f:
            f.write(f"Name: {name}\nAge: {age}\n")

        return f"File generated at: {file_path}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
