from flask_app import app, bcrypt
from flask import render_template, redirect, session, request
from flask_app.models.model_headshop import Headshop

# this file contains headshop routes: login?,create,show,edit,update,delete

# login?

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
    Headshop.create(data)
    return redirect('/dashboard')

# show

# edit

# update

# delete