#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 23:45:54
# @Author  : Racter Liu (racterub) (racterub@gmail.com)
# @Link    : https://racterub.me
# @License : MIT

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("config")


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8989)
