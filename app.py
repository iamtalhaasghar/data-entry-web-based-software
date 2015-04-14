#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from database import db_session
from database import init_db
from models import Person
import logging

init_db()

app = flask.Flask(__name__)

app.logger.setLevel(logging.DEBUG)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def hello_world():
    q = Person.query.all()
    t = ''
    lista = []
    for person in q:
        t += ' ' + person.lastname
        lista.append(person)
    print "Hola", lista
    print flask.render_template('index.html', people=lista)

    return flask.render_template('index.html', people=q)


if __name__ == '__main__':
    app.run(debug=True)
