from app import app, db_session
from ..data.candles import Candle
from ..data.ktds import Ktd
from ..data.events import Event
from ..data.games import Game
from flask import render_template, redirect
from requests import get


@app.route('/forum')
def forum():
    db_sess = db_session.create_session()
    candles = db_sess.query(Candle).all()
    games = db_sess.query(Game).all()
    ktds = db_sess.query(Ktd).all()
    events = db_sess.query(Event).all()
    cards = candles + games + ktds + events
    all_cards = []
    for i in range(0, len(cards), 6):
        page = []
        for j in range(0, len(cards[i: i + 6]), 2):
            row = []
            row.append(cards[i: i + 6][j])
            try:
                row.append(cards[i: i + 6][j + 1])
            except:
                pass
            page.append(row)
        all_cards.append(page)
    return render_template("forum/forum.html", title="Форум", all_cards=all_cards, len=len)