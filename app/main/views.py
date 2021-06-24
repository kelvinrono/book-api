from flask import render_template,request,redirect,url_for
from flask import render_template
from ..requests import get_books
from . import main
from .form import ReviewForm
import markdown2
from flask_login import login_required, current_user


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    current_books = get_books('current')


    return render_template('index.html', current=current_books)

@main.route('/book/review/new/<int:id>' , methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    book = get_book(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        new_review = Review(book_id =book.id,book_title=title,image_path=book.poster,book_review=review,user=current_user)
        
        new_review.save_review()
        return redirect(url_for('.book',id= book.id ))

    title = f'{book.title} review'
    return render_template('new_review.html',title = title, review_form=form, book=book)

@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        about(404)
    format_review = markdown2.markdown(review.book_review,extras=["code-friendly","fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)


