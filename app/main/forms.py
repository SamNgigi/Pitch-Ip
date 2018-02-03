from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import Required, Email
from ..models import User


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.',
                        validators=[Required()])
