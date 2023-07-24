from flask import render_template, redirect, session #render template; comes from flask dependency that we installed in PIPfile
from flask_app import app # this is the same as the server.py declaration; we created the instance in __init__, and gets shared throughout the project
from flask_app.models.model_headshop import Headshop

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'dispensary_id' not in session:
        return redirect('/')
    
    dispensary = Headshop.get_one({'id': session['dispensary_id']})
    return render_template('dashboard.html', dispensary = dispensary)