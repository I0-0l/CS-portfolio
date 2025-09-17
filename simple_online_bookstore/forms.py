from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,DecimalField
from flask_wtf.file import FileAllowed,FileRequired, FileField
from wtforms.validators import InputRequired,EqualTo

class RegistrationForm(FlaskForm):
    user_id = StringField("User id:",
        validators=[InputRequired()])
    password = PasswordField("Password:",
        validators=[InputRequired()])
    password2 = PasswordField("Repeat password:",
        validators=[InputRequired(),EqualTo("password")])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    user_id = StringField("User id:",
        validators=[InputRequired()])
    password = PasswordField("Password:",
        validators=[InputRequired()])
    submit = SubmitField("Submit")

class UploadForm(FlaskForm):
    book_name = StringField("Book's name:",
            validators=[InputRequired()])
    price = DecimalField("Prices:",
            validators=[InputRequired()])
    description = StringField("Description:",
            validators=[InputRequired()])
    type = StringField("Type:",
            validators=[InputRequired()])    
    stockpiles = IntegerField("stockpiles:",
            validators=[InputRequired()])
    img_loc = StringField("Img_loc(blablabla.jpg):",
             validators=[InputRequired()]) 
    book_cover = FileField("Book cover(only jpg)", validators=[FileAllowed(['jpg', 'jpeg'], "file please")])
    submit=SubmitField("Submit")
    
