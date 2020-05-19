#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 23:45:54
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.me
# @License : MIT

from flask import Flask, render_template, request, url_for, redirect, session, send_from_directory, send_file, make_response

app = Flask(__name__)
app.secret_key = "test"
DEBUG = True
PORT = 8989


@app.route("/")
def index():
    return "index of /"


# in-url param
@app.route("/db/<dbname>/<int:dbid>")
def db(dbname, dbid):
    return "dbname: %s, dbid: %s" % (dbname, dbid+123)

# http get param
@app.route("/get/")
def get():
    name = request.args.get("name")
    passwd = request.args.get("passwd")
    return "name: %s, password: %s" % (name, passwd)


@app.route("/post/")
def post():
    name = request.form["name"]
    passwd = request.form["passwd"]
    return "name: %s, password: %s" % (name, passwd)


# implement login
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        try:
            if (request.form["username"] == "test" and request.form["password"] == "test"):
                session["user"] = request.form["username"]
                return "Success"
            else:
                return redirect(url_for("login", next=request.endpoint))
        except ValueError:
            return "Something broke", 400
    else:
        return render_template("login.html")

# session
@app.route("/admin/")
def admin():
    if ('user' not in session):
        return redirect(url_for("login", next=request.endpoint))
    return "admin!"


@app.route("/logout")
def logout():
    if ('user' in session):
        session.pop("user", None)
        return "Logout"
    else:
        return redirect(url_for("index"))

# serve static file
@app.route("/robots.txt")
def robot():
    return send_from_directory("static", "robots.txt")

# make_response
@app.route("/makeresponse/")
def makeresp():
    resp = make_response("test", 200)
    resp.headers['X-Author'] = "ITAC"
    return resp

# Jinja
@app.route("/jinja/<name>")
def jinja(name):
    return render_template("index.html", title=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
