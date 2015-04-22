#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crudapp import app

import flask

import crudapp.model.model as model

import curl

curl.add_curl(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    model.session.remove()


@app.route('/')
def index():
    q = model.all_people()
    return flask.render_template('index.html', people=q)


@app.route('/new_person', methods=['POST'])
def add_person():
    model.add_person(firstname=flask.request.form['firstname'],
                     lastname=flask.request.form['lastname'])
    return flask.redirect(flask.url_for('index'))


@app.route('/delete_person', methods=['POST'])
def delete_person():
    model.delete_person(person_id=flask.request.form['person_id'])

    return flask.redirect(flask.url_for('index'))


@app.route('/edit_person', methods=['POST'])
def edit_person():
    model.edit_person(person_id=flask.request.form['person_id'],
                      firstname=flask.request.form['firstname'],
                      lastname=flask.request.form['lastname'])
    return flask.redirect(flask.url_for('index'))


# This adds curl-like logging

if __name__ == '__main__':
    app.run(debug=True)
