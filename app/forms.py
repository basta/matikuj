from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SampleForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name')
    email = StringField('Email')
    submit = SubmitField('Submit')

class SessionCreator(FlaskForm):
    text = StringField('Name:')
    join = SubmitField("Join")
    create = SubmitField("Create")