#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import logging

import database
from models import Person
import curl

database.init_db()
session = database.db_session

app = flask.Flask(__name__)

app.logger.setLevel(logging.DEBUG)

curl.add_curl(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


@app.route('/')
def index():
    q = Person.query.all()
    return flask.render_template('index.html', people=q)


@app.route('/new_person', methods=['POST'])
def add_person():
    np = Person(firstname=flask.request.form['firstname'],
                lastname=flask.request.form['lastname'])
    session.add(np)
    session.commit()
    return index()


@app.route('/delete_person', methods=['POST'])
def delete_person():
    p = session.query(Person).filter_by(
        person_id=flask.request.form['person_id']
    ).one()
    session.delete(p)
    session.commit()
    return flask.redirect(flask.url_for('index'))


@app.route('/edit_person', methods=['POST'])
def edit_person():
    p = session.query(Person).filter_by(
        person_id=flask.request.form['person_id']
    ).one()
    p.lastname = flask.request.form['lastname']
    p.firstname = flask.request.form['firstname']
    session.commit()
    return flask.redirect(flask.url_for('index'))


# This adds curl-like logging

if __name__ == '__main__':
    app.run(debug=True)
