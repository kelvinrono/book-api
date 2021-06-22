from flask import render_template
from . import main
from ..requests import get_books,get_book,search_book


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''



    return render_template('index.html')

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

