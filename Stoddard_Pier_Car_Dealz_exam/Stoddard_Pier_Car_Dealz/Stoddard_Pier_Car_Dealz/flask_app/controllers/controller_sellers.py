from flask_app import app
from flask_app.models.model_seller import Seller
from flask_app.models.model_deal import Deal   #added this import for deal data needed for the get_all class
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, redirect, request, session, flash


@app.route('/')
def index():
    if 'id' in session:
        return redirect('/dashboard')
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    if not Seller.validate(request.form):
        return redirect('/')
    pass_hash=bcrypt.generate_password_hash(request.form['password'])
    data={
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password': pass_hash
    }
    print(data)
    seller_id=Seller.create(data)
    session['id']=seller_id
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    seller_in_db=Seller.get_by_email({'email':request.form['email']})
    if not seller_in_db:
        flash("*Invalid login credentials", "login_errors")
        return redirect('/')
    if not bcrypt.check_password_hash(seller_in_db.password, request.form['password']):
        flash("*Invalid login credentials", "login_errors")
        return redirect('/')
    session['id']=seller_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'id' not in session:
        return redirect('/')
    logged_in_seller = Seller.get_one({'id': session['id']})
    all_deals = Deal.get_all({'seller_id': logged_in_seller.id})
    return render_template('dashboard.html', seller=logged_in_seller, all_deals=all_deals)


@app.route('/logout')
def logout():
    session.clear()
    flash('Successfully logged out', 'logout')
    return redirect('/')