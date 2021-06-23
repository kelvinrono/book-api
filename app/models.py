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
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey('books.id',ondelete='CASCADE'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id',ondelete='CASCADE'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    def saveComment(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def getComment(cls, blog_id):
        comments = Comment.query.filter_by(blook_id=book_id).all()
        return comments
    def deleteComment(self):
        db.session.delete(self)
        db.session.commit()
    def __repr__(self):
        return f'Comments: {self.comment}'
 




class Book:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self,author,title,description,book_image,amazon_product_url):
        self.author = author
        self.title, = title,
        self.description = description
        self.book_image = book_image
        self.amazon_product_url = amazon_product_url


 
