#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import logging

import database
from models import Person
import curl

database.init_db()

app = flask.Flask(__name__)

app.logger.setLevel(logging.DEBUG)


@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()


@app.route('/')
def index():
    q = Person.query.all()
    return flask.render_template('index.html', people=q)


@app.route('/new_person', methods=['POST'])
def add_person():
    # show the post with the given id, the id is an integer
    np = Person(firstname=flask.request.form['firstname'],
                lastname=flask.request.form['lastname'])
    database.db_session.add(np)
    database.db_session.commit()
    return index()

# This adds curl-like logging
curl.add_curl(app)

if __name__ == '__main__':
    app.run(debug=True)
