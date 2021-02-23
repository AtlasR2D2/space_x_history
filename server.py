import requests
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField

SPACE_X_URL = "https://api.spacexdata.com/v3/history"
WEBPAGE_OWNER = "Mike"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

@app.route('/')
def home():
    response = requests.get(SPACE_X_URL)
    space_x_data = response.json()
    return render_template("index.html", space_x_data=space_x_data, webpage_owner=WEBPAGE_OWNER)

if __name__ == "__main__":
    app.run(debug=True)