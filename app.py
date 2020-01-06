# Project Title: NRD Portfolio "Static" Final
# SQL Alchemy for Flask/AWS Deployment.
# Coder: Neil Denning


from flask import Flask, render_template, redirect, request, session, flash

from datetime import datetime

'''
C - create - INSERT
R - read - SELECT
U - update - UPDATE
D - delete - DELETE
'''

app = Flask(__name__)


@app.route("/")
def home_page():
        return render_template("mainnew_fixbug.html")

@app.route("/frontend_proj")
def frontend_proj():
    return render_template("frontend_proj.html")

@app.route("/backend_proj")
def backend_proj():
    return render_template("backend_proj.html")

@app.route("/jaynedoe_proj")
def jaynedoe_proj():
    return render_template("jaynedoe_proj.html")

@app.route("/jaynedoe_original")
def jaynedoe_original():
    return render_template("jaynedoe_original.html")

@app.route("/aboutpython_proj")
def aboutpython_proj():
    return render_template("aboutpython_proj.html")

@app.route("/aboutpython_original")
def about_python_original():
        return render_template("aboutpython_original.html")

@app.route("/internet_proj")
def internet_proj():
    return render_template("internet_proj.html")

@app.route("/internet_original")
def internet_original():
        return render_template("internet_original.html")


@app.route("/dojo_survey_main_preview")
def dojo_survey_main_preview():
        return render_template("dojo_survey_main_preview.html")

@app.route("/dojo_tweet_main_preview")
def dojo_tweet_main_preview():
        return render_template("dojo_tweet_main_preview.html")

@app.route("/quotes")
def quotes():
        return render_template("quotes.html")

@app.route("/algorithms_prev")
def algorithms_prev():
        return render_template("algorithms_prev.html")

@app.route("/ps_prev")
def ps_prev():
        return render_template("ps_prev.html")



if __name__ == "__main__":
        app.run(debug=True)
