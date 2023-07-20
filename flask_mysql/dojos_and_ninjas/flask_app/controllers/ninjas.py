from flask_app import app
from flask import redirect, render_template, request
from ..models.dojo import Dojo
from ..models.ninja import Ninja

# @app.route('/ninjas')
# def ninjas():
#     return render_template('ninjas.html', all_ninjas=Ninja.get_all())

@app.route('/ninjas')
def ninjas():
    all_ninjas = Ninja.get_all()
    all_dojos = Dojo.get_all()
    return render_template('ninjas.html', all_ninjas=all_ninjas, all_dojos=all_dojos)

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "age": request.form['age'],
        "dojo_id": request.form['dojo_id'],
        "weapon_of_choice": request.form['weapon_of_choice']
    }
    ninja_id = Ninja.save(data)
    return redirect('/ninjas')