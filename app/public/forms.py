# crue-name-python-flask

from flask_wtf import FlaskForm # pip install flask_wtf
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FormName(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired(), ])
    email = StringField('Enter your email', validators=[DataRequired(), ])
    phone = StringField('Enter your phone number', validators=[DataRequired(), ])
    submit = SubmitField('ADD NAME')

