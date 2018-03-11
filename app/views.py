from app import app
from app import db
from flask import render_template, request, jsonify
from app.models import * #todo - import specific objects
import json
import flask
    
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/route2", methods=["GET", "POST"])
def route2():
    x = request.args()
    return x