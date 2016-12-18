from bs_app import app
from flask import render_template, redirect, url_for
from . scripts import bs_script


@app.route("/")
def index():
    return render_template("press_button.html")


@app.route("/press_button", methods=["POST"])
def press():
    return redirect(url_for("congrats"))


@app.route("/congrats", methods=["GET"])
def congrats():
    greeting = bs_script.hi()
    title = bs_script.site_name()
    return render_template("congrats.html", greeting=greeting, title=title)
