from flask import render_template,request,redirect,url_for

from flask import render_template
from ..requests import get_books
from . import main
from ..requests import get_books


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    current_books = get_books('current')


    return render_template('index.html', current=current_books)

@main.route('/book/<int:id>')
def book(title):
    '''
    View book page function that returns the book details page and its data
    '''
    book = get_book(title)
    title = f'{book.title}'
    reviews = Review.get_reviews(book.title)
    return render_template('book.html',title = title,book = book,reviews = reviews)
@main.route('/search/<book_name>')
def search(book_name):
    '''
    View function to display the search results
    '''
    book_name_list = book_name.split(" ")
    book_name_format = "+".join(book_name_list)
    searched_books = search_book(book_name_format)
    title = f'search results for {book_name}'
    return render_template('search.html',books = searched_books)    




