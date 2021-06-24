from app.requests import get_books
from flask import render_template,request,redirect,url_for,flash
from . import main
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
from .form import CommentForm
from ..models import Book,Comment,User



# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    current_books = get_books('current')


    return render_template('index.html', current=current_books)

@main.route('/comment/new/<int:id>', methods=['GET', 'POST'])
@login_required
def newComment(id):
    book = Book.query.filter_by(id = id).all()
    bookComments = Comment.query.filter_by(book_id=id).all()
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        new_comment = Comment(book_id=id, comment=comment, user=current_user)
        new_comment.saveComment()
    return render_template('newComment.html', book=book, book_comments=bookComments, comment_form=comment_form)
 
@main.route('/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def deleteComment(id):
    comment =Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()
    flash('comment succesfully deleted')
    return redirect (url_for('main.allBooks'))

