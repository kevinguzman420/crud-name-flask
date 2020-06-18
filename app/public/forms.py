# crud-name-python-flask

from flask_wtf import FlaskForm # pip install flask_wtf
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class FormName(FlaskForm):
    name = StringField('Enter your name:', validators=[DataRequired(message="Ingrese un nombre por favor."), ])
    email = StringField('Enter your email', validators=[DataRequired(message="Ingrese un correo por favor."), Email(message="Ingrese un correo válido por favor.", )])
    phone = IntegerField('Enter your phone number', validators=[DataRequired(message="Ingrese un número por favor."), ])


