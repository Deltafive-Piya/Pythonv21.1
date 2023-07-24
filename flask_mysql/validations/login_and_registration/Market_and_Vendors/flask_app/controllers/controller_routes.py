from flask import render_template, redirect, session #render template; comes from flask dependency that we installed in PIPfile
from flask_app import app # this is the same as the server.py declaration; we created the instance in __init__, and gets shared throughout the project
from flask_app.models.model_vendor import Vendor


from flask import render_template, redirect, session
from flask_app import app
from flask_app.models.model_vendor import Vendor

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'vendor_id' not in session:
        return redirect('/')

    # Retrieve the vendor data from the session
    vendor_id = session['vendor_id']
    vendor = Vendor.get_one({'id': vendor_id})
    
    if not vendor:
        return redirect('/')

    return render_template('dashboard.html', vendor=vendor)
