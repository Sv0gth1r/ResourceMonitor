from flask import Flask, render_template, jsonify
from stats import *

app = Flask(__name__)
c_stats = Stats()
print(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/stats")
def render_stats():
    return jsonify(c_stats.get_stats())
