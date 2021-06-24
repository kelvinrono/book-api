from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,TextAreaField,BooleanField
from wtforms.validators import Required,Email

from ..models import User

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Book review')
    submit = SubmitField('Submit')

