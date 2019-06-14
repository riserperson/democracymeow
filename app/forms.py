from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import ValidationError, DataRequired

class Login(FlaskForm):
    pw = PasswordField('Password', validators=[DataRequired()])
