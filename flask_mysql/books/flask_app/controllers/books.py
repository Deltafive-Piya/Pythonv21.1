from flask_app import app
from flask import redirect, render_template,request
from ..models.author import Author
from ..models.book import Book


@app.route('/books')
def books():
    return render_template('books.html',all_books=Book.get_all())

@app.route('/create/book',methods=['POST'])
def create_book():
    data = {
        "title":request.form['title'],
        "num_of_pages": request.form['num_of_pages']
    }
    book_id = Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        "id":id
    }
    return render_template('show_books.html',book=Book.get_by_id(data),unfavorited_authors=Author.unfavorited_authors(data))

@app.route('/join/author',methods=['POST'])
def join_author():
    data = {
        'authors_id': request.form['authors_id'],
        'books_id': request.form['books_id']
    }
    Author.add_favorite(data)
    return redirect(f"/books/{request.form['books_id']}")