<<<<<<< HEAD
from flask import render_template,request,redirect,url_for
from flask import render_template
from ..requests import get_books
from . import main
from .form import ReviewForm
import markdown2
from flask_login import login_required, current_user
from . import main
from ..requests import get_books,search_book
from flask import render_template,request,redirect,url_for,abort
from ..requests import get_books
from . import main
from ..models import User
from .forms import UpdateProfile
from .. import db
from flask_login import login_required, current_user
# from flask_login import login_required

=======


from flask import render_template,request,redirect,url_for,flash,abort
from . import main
from .. import db
from flask_login import login_user,logout_user,login_required,current_user
from .form import CommentForm,ReviewForm
from ..models import Book,Comment,User



from ..requests import get_books

 
import markdown2


from ..requests import get_books

from .forms import UpdateProfile
# from flask_login import login_required


>>>>>>> 0dd6789d5bad9a3f9f075c9d5419b871ca134930


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    current_books = get_books('current')


    return render_template('index.html', current=current_books)

<<<<<<< HEAD
=======

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

>>>>>>> 0dd6789d5bad9a3f9f075c9d5419b871ca134930
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


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
<<<<<<< HEAD
=======

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/book/<int:id>')
def book(id):

    '''
    View book page function that returns the book details page and its data
    '''
    book = get_book(id)
    title = f'{book.title}'
    reviews = Review.get_reviews(book.id)
>>>>>>> 0dd6789d5bad9a3f9f075c9d5419b871ca134930

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/book/<int:id>')
def book(id):

    '''
    View book page function that returns the book details page and its data
    '''
    book = get_book(id)
    title = f'{book.title}'
    reviews = Review.get_reviews(book.id)

    return render_template('book.html',title = title,book = book,reviews = reviews)