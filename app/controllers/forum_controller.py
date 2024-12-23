from app import app, db_session
from ..data.methodics import Method
from flask import render_template, redirect
from requests import get


@app.route('/forum')
def forum():
    db_sess = db_session.create_session()
    methodics = db_sess.query(Method).all()
    all_cards = []
    for i in range(0, len(methodics), 6):
        page = []
        for j in range(0, len(methodics[i: i + 6]), 2):
            row = []
            row.append(methodics[i: i + 6][j])
            try:
                row.append(methodics[i: i + 6][j + 1])
            except:
                pass
            page.append(row)
        all_cards.append(page)
    return render_template("forum/forum.html", title="Форум", all_cards=all_cards, len=len)


@app.route('/forum/methodics/<id>')
def methodics(id):
    db_sess = db_session.create_session()
    methodics = db_sess.query(Method).all()
    for i in methodics:
        if int(id) == i.id:
            title = i.title
            description = i.description
            period = i.period
            type = i.type_of_methodic
            invetory = i.inventory
            age = i.age
            method = {"title": title, 
                      "type": type, 
                      "period": period, 
                      "age": age, 
                      "inventory": invetory, 
                      "description": description}
            return render_template("forum/methodics.html", title=title, len=len, method=method)