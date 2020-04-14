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

# @app.route("/")
# def index():
#     return render_template("index.html", title="Index of /")


# @app.route("/table/")
# def table():
#     return render_template("table.html", lst=['a', 'b', 'c', 'd'], combine=True)

# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('db', dbname='John Doe', dbid='123'))


@app.route("/")
def index():
    return "index of /"


# in-url param
@app.route("/db/<dbname>/<int:dbid>")
def db(dbname, dbid):
    return "dbname: %s, dbid: %s" % (dbname, dbid+123)

# http get param
@app.route("/user/")
def user():
    name = request.args.get("name")
    passwd = request.args.get("passwd")
    return "name: %s, password: %s" % (name, passwd)

# implement login
@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if (username and password):
            if (username == "test" and password == "test"):
                session["user"] = username
                return "Success"
            else:
                return redirect(url_for("login", next=request.endpoint))
        return "%s %s" % (username, password)

    else:
        return render_template("login.html")

# session
@app.route("/admin/")
def admin():
    if (not session["user"]):
        return redirect(url_for("login", next=request.endpoint))
    return "admin!"

# serve static file
@app.route("/robots.txt")
def robot():
    return send_from_directory("static", "robots.txt")

# download file
@app.route("/download")
def download():
    return send_file("static/test")

# make_response
@app.route("/makeresponse/")
def makeresp():
    resp = make_response("test", 200)
    resp.headers['X-Author'] = "ITAC"
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
