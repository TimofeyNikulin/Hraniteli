from app import app, db_session
from flask import render_template, redirect
from requests import get
from ..forms.add_methodic_form import MethodForm
from ..data.methodics import Method


@app.route('/add_game', methods=["GET", "POST"])
def add_game():
    form = MethodForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        try:
            game = Method(
                title=form.title.data,
                description=form.description.data,
                age=form.age.data,
                inventory=form.inventory.data,
                period=form.period.data,
                type_of_methodic=form.type_of.data
            )
            db_sess.add(game)
            db_sess.commit()
            return redirect('/add_game')
        except:
            return render_template('education/addGame.html', form=form, message='Что-то пошло не так, попробуйте перезаполнить поля')
    return render_template('education/addGame.html', form=form, message='')


@app.route('/education')
def education():
    return render_template('education/education.html', title="Обучение")


@app.route('/education/orgPeriod')
def org_period():
    db_sess = db_session.create_session()
    methods = db_sess.query(Method).all()
    take_methods = []
    for method in methods:
        if method.period == "организационный":
            take_methods.append(method)
    return render_template('education/orgPeriod.html', games=take_methods, title="Организационный период")


@app.route('/education/middlePeriod')
def middle_period():
    db_sess = db_session.create_session()
    methods = db_sess.query(Method).all()
    take_methods = []
    for method in methods:
        if method.period == "основной":
            take_methods.append(method)
    return render_template('education/middlePeriod.html', games=take_methods, title="Основной период")


@app.route('/education/endPeriod')
def end_period():
    db_sess = db_session.create_session()
    methods = db_sess.query(Method).all()
    take_methods = []
    for method in methods:
        if method.period == "заключительный":
            take_methods.append(method)
    return render_template('education/endPeriod.html', games=take_methods, title="Заключительный этап")
