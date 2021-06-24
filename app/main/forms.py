from wtforms import StringField,TextAreaField, SubmitField, SelectField
from wtforms.validators import Required
from flask_wtf import FlaskForm

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Update details about you here',validators = [Required()])
    submit = SubmitField('Submit')