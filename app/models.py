from enum import unique
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email=db.Column(db.String(255), unique=True, index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
                
    @password.setter
    def password(self, password):
            self.pass_secure=generate_password_hash(password)
        
    def verify_password(self,password):
                    return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

# class Book(db.Model):
#     '''
#     Book class to define book objects.
#     '''
#     def __init__(self,title,author,description,book_image,published_date,):
#         self.title = title
#         self.author = author
#         self.description = description
#         self.book_image ="https://storage.googleapis.com/du-prd/books/images/" + book_image
#         self.published_date =published_date 

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    book_id = db.Column(db.Integer)
    book_title = db.Column(db.String)
    image_path = db.Column(db.String)
    book_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(book_id=id).all()
        return reviews

class Book:
    '''
    book class to define book Objects
    '''

    def __init__(self,author,title,description,book_image,amazon_product_url):
        self.title, = title,
        self.author = author
        self.description = description
        self.book_image = book_image
        self.amazon_product_url = amazon_product_url


 
