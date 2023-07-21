from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.model_headshop import Headshop
# this file contains headshop routes: login?,create,show,edit,update,delete


#login?


#create (action route)
@app.route('/headshop/create')
def headshop_create():
    #clone the request dictionary
    data = {**request.form}
    #validate-targets the object in model file
    is_valid = Headshop.validate(data)
    if is_valid == False:
        return redirect('/')
    
    #hash the password

    #update the password in the data dictionary

    #create the dispensary

    return redirect('/dashboard')

#show


#edit


#update


#delete