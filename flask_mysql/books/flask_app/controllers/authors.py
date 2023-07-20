from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book


@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html',all_authors=Author.get_all())

@app.route('/create/author',methods=['POST'])
def create_author():
    data = {
        "name": request.form['name']
    }
    author_id = Author.save(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def show_author(id):
    author_data = {
        "id": id
    }
    unfavorited_books_data = {
        "id": id
    }
    return render_template('show_authors.html', author=Author.get_by_id(author_data), unfavorited_books=Book.unfavorited_books(unfavorited_books_data))

@app.route('/join/book',methods=['POST'])
def join_book():
    data = {
        'authors_id': request.form['authors_id'],
        'books_id': request.form['books_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['authors_id']}")