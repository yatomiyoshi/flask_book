from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


class UserForm(FlaskForm):
    username = StringField(
        "username",
        validators=[
            DataRequired(message="Username is required."),
            length(max=30, message="Username length must be shorter than 30."),
        ],
    )
    email = StringField(
        "email address",
        validators=[
            DataRequired(message="email address is required."),
            Email(message="Enter with email style."),
        ],
    )
    password = PasswordField(
        "password", validators=[DataRequired(message="Password is required.")]
    )
    submit = SubmitField("New")
