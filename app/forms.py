from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
  openid = TextField('openid', validators = [DataRequired()])
  remember_me = BooleanField('remember_me', default = False)

class EditForm(Form):
  nickname = TextField('nickname', validators = [DataRequired()])
  about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])