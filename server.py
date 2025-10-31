from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

# Endpoints


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page>")
def html_page(page=""):
    return render_template(f"{page}.html")


@app.route("/submit_form", methods=("GET", "POST"))
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        return redirect("/thankyou")
    else:
        return "Something went wrong"
