from app import app, db_session
from flask import render_template, redirect
from requests import get
from ..forms.add_game_form import GameForm
from ..data.games import Game


@app.route('/add_game', methods=["GET", "POST"])
def add_game():
    form = GameForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        try:
            game = Game(
                title=form.title.data,
                description=form.description.data,
                age=form.age.data,
                inventory=form.inventory.data,
                period=form.period.data,
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
    games = db_sess.query(Game).all()
    take_games = []
    for game in games:
        if game.period == "организационный":
            take_games.append(game)
    return render_template('education/orgPeriod.html', games=take_games, title="Организационный период")


@app.route('/education/middlePeriod')
def middle_period():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    take_games = []
    for game in games:
        if game.period == "основной":
            take_games.append(game)
    return render_template('education/middlePeriod.html', games=take_games, title="Основной период")


@app.route('/education/endPeriod')
def end_period():
    db_sess = db_session.create_session()
    games = db_sess.query(Game).all()
    take_games = []
    for game in games:
        if game.period == "заключительный":
            take_games.append(game)
    return render_template('education/endPeriod.html', games=take_games, title="Заключительный этап")
