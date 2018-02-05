from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required
from ..models import Pitch


class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    body = TextAreaField('Enter your pitch here', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    category = RadioField('Pick Category',
                          choices=[('business', 'business'),
                                   ('jobs', 'jobs')],
                          validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about yourself.',
                        validators=[Required()])
