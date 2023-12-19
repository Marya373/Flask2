from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf import FlaskForm


class UserRegistration(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=20)])
    date = DateField('DateBirth', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    consent_processing_personal_data = BooleanField('Confirm Processing Personal Data', validators=[DataRequired()])
