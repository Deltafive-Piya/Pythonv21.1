from flask import render_template, redirect, session, request
from flask_app import app, bcrypt
from flask_app.models.model_vendor import Vendor

# this file contains Vendor routes: login?,Logout,create,show,edit,update,delete

# login
@app.route('/vendor/login', methods=['POST'])
def vendor_login():
    if request.method == 'POST':
        data = {**request.form}
        is_valid = Vendor.validate_login(data)
        if not is_valid:
            return redirect('/')
        return redirect('/dashboard')
    else:
        # In case the route is accessed through GET method, redirect to the homepage
        return redirect('/')

# Logout
@app.route('/vendor/logout')
def vendor_logout():
    del session['vendor_id']
    return redirect('/')

# create (action route)
@app.route('/vendor/create', methods=['POST'])
def vendor_create():
    # clone the request dictionary
    data = {**request.form}
    # validate - targets the object in the model file
    is_valid = Vendor.validate(data)
    if not is_valid:
        return redirect('/')

    # hash the password
    hash_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # update the password in the data dictionary
    data['password'] = hash_pw
    # create the vendor
    id = Vendor.create(data)
    session['vendor_id'] = id
    # This Dashboard is created in controller_routes
    return redirect('/dashboard')

# show

# edit

# update

# delete