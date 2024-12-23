from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired


class MethodForm(FlaskForm):
    title = StringField(label="Название игры", name="title", id="title",
                       validators=[InputRequired()])
    description = TextAreaField(label="Описание", name="description",
                          id="description", validators=[InputRequired()])
    age = StringField(label="Возраст детей (младшие, средние, старшие)", name="age", id="age")
    inventory = StringField(label="Необходимый ивентарь (при необходимости)", name="inventory", id="inventory")
    period = StringField(label="Период (организационный, основной, заключительный)", name="period", id="period")
    type_of = StringField(label="Тип методики (Игра, КТД, Мероприятие, Свечка)", name="type", id="type")