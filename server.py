from flask import Flask
from flask import render_template

app = Flask(__name__)

# Endpoints


@app.route("/")
def my_home():
    return render_template("index.html")
