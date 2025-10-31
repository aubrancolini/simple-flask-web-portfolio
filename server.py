from flask import Flask
from flask import render_template, request, redirect
import csv

app = Flask(__name__)


# functions


# Write to csv data collected by contact me form
def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database_csv,
            delimiter=",",
            quotechar=" ",
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


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
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou")
        except Exception as e:
            return f"Did not save to database. Error: {e}"
    else:
        return "Something went wrong"
