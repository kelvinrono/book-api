from flask_wtf import FlaskForm
<<<<<<< HEAD
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required,Email
from ..models import User

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')
=======
from wtforms import StringField,TextAreaField,SubmitField,ValidationError,TextAreaField,BooleanField,
from wtforms.validators import Required,Email
from ..models import User

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')
>>>>>>> 0dd6789d5bad9a3f9f075c9d5419b871ca134930
