# from flask import render_template,redirect,request
from flask_app.controllers.burgers import burgers
from flask_app import app
# ...server.py

# from flask_app.models.burger import Burger

if __name__=="__main__":
    app.run(host="localhost", port=5001, debug=True)