from flask import render_template,request,redirect,url_for

from flask import render_template
from ..requests import get_books
from . import main
from ..requests import get_books,get_book,search_book


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    current_books = get_books('current')


    return render_template('index.html', current=current_books)


