from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, DateField
from wtforms.validators import InputRequired, DataRequired


class PersonalDataForm(FlaskForm):
    name = StringField(label="Имя", name="name", id="name",
                       validators=[InputRequired()])
    surname = StringField(label="Фамилия", name="surname",
                          id="surname", validators=[InputRequired()])
    patronymic = StringField(
        label="Отчество", name="patronymic", id="patronymic")
    age = IntegerField(label="Возраст", name="age", id="age",
                       validators=[InputRequired()])