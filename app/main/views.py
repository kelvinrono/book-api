from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_books,get_book,search_book


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    fiction_books= get_books('fiction')
    horror_books = get_books('horror')
    recent_published_books = get_books('recent_published')
    title = 'Home - Welcome to The best Book Review Website Online'
    search_book = request.args.get('book_query')
    if search_book:
        return redirect(url_for('.search',book_name =search_book))
    else:
        return render_template('index.html', title = title,fiction = fiction_books, horror= horror_books, recent_published = recent_published_books )

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

