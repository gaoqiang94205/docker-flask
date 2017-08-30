from flask.ext.wtf import Form
from wtforms import TextField,PasswordField, StringField, SubmitField
from wtforms.validators import Required,length, DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    #submit = SubmitField('submit')
