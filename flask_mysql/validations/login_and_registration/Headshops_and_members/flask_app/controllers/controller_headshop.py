from flask import render_template, redirect, session, request
from flask_app import app, bcrypt
from flask_app.models.model_headshop import Headshop

# this file contains headshop routes: login?,Logout,create,show,edit,update,delete

# login
@app.route('/dispensary/login', methods=['POST'])
def dispensary_login():
    if request.method == 'POST':
        data = {**request.form}
        is_valid = Headshop.validate_login(data)
        if not is_valid:
            return redirect('/')
        return redirect('/dashboard')
    else:
        # In case the route is accessed through GET method, redirect to the homepage
        return redirect('/')

# Logout
@app.route('/dispensary/logout')
def dispensary_logout():
    del session['dispensary_id']
    return redirect('/')

# create (action route)
@app.route('/headshop/create', methods=['POST'])
def headshop_create():
    # clone the request dictionary
    data = {**request.form}
    # validate - targets the object in the model file
    is_valid = Headshop.validate(data)
    if not is_valid:
        return redirect('/')

    # hash the password
    hash_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    # update the password in the data dictionary
    data['password'] = hash_pw
    # create the dispensary
    id = Headshop.create(data)
    session['dispensary_id'] = id
    # This Dashboard is created in controller_routes
    return redirect('/dashboard')

# show

# edit

# update

# delete