#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route("/user/<name>")
def hello_world(name):
    return render_template('index.html', usr=name)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
