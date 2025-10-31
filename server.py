from flask import Flask
from flask import render_template
import request

app = Flask(__name__)

# Endpoints


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page>")
def html_page(page=""):
    return render_template(f"{page}.html")
