from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.model_deal import Deal
from flask_app.models.model_seller import Seller
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/deals/new')
def new_deal():
    if 'id' not in session:
        return redirect('/')
    logged_in_seller=Seller.get_one({'id':session['id']})
    all_deals=logged_in_seller.deals
    print(all_deals)
    return render_template('create.html', all_deals=all_deals)


@app.route('/deals/create', methods=['POST'])
def create_deal():
    if 'id' not in session:
        return redirect('/')
    if not Deal.validate(request.form):
        print('Form data not valid')
        return redirect('/deals/new')

    data = {
        'model': request.form['model'],
        'price': request.form['price'],
        'make': request.form['make'],
        'year': request.form['year'],
        'description': request.form['description'],
        'seller_id': session['id']
    }
    print("Data to be created:", data)

    deal_id = Deal.create(data)
    print("Deal created with ID:", deal_id)

    return redirect('/dashboard')


@app.route('/deals/<int:id>')
def get_deal(id):
    if 'id' not in session:
        return ('/')
    logged_in_seller=Seller.get_one({'id':session['id']})
    selected_deal=Deal.get_one({'id':id})
    return render_template('deal.html', seller=logged_in_seller, deal=selected_deal)


@app.route('/deals/update/<int:id>', methods=['POST'])
def update_deal(id):
    if 'id' not in session:
        return redirect('/')
    if not Deal.validate(request.form):
        return redirect(f"/deals/edit/{id}")
    data={
        'id':id,
        'model':request.form['model'],
        'year':request.form['year'],
        'price':request.form['price'],
        'make':request.form['make'],
        'purchased':request.form['purchased'],
        'description':request.form['description']
    }
    Deal.update(data)
    return redirect('/dashboard')


@app.route('/deals/edit/<int:id>')
def edit_deal(id):
    if 'id' not in session:
        return redirect('/')
    selected_deal=Deal.get_one({'id':id})
    return render_template('update.html', deal=selected_deal)


@app.route('/deals/delete/<int:id>')
def delete_deal(id):
    if 'id' not in session:
        return redirect('/')
    Deal.delete({'id':id})
    return redirect('/dashboard')