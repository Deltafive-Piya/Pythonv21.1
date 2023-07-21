from flask_app import app
from flask import render_template, redirect, session, request
# this file contains headshop routes: login?,create,show,edit,update,delete


#login?


#create (action route)
@app.route('/dispensary/create')
def dispensary_create():
    #clone the request dictionary
    data = {**request.form}
    #validate-targets the object in model file
    
    #hash the password

    #update the password in the data dictionary

    #create the dispensary

    return redirect('/dashboard')

#show


#edit


#update


#delete