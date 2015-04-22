#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The controller receives commands from the views,
    sends commands to the model,
    chooses the views to send,
    and sends the views to the user.

    This controller is powered by Flask.

    The views are Jinja2 templates and static files.

"""

import flask

import crudapp.model.db_model as dbmodel


def def_control(app):

    # This is part of the db_model init
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        dbmodel.session.remove()

    @app.route('/')
    def index():
        q = dbmodel.all_people()
        return flask.render_template('index.html', people=q)

    @app.route('/add_person', methods=['POST'])
    def add_person():
        dbmodel.add_person(firstname=flask.request.form['firstname'],
                           lastname=flask.request.form['lastname'])
        return flask.redirect(flask.url_for('index'))

    @app.route('/delete_person', methods=['POST'])
    def delete_person():
        dbmodel.delete_person(person_id=flask.request.form['person_id'])

        return flask.redirect(flask.url_for('index'))

    @app.route('/edit_person', methods=['POST'])
    def edit_person():
        dbmodel.edit_person(person_id=flask.request.form['person_id'],
                            firstname=flask.request.form['firstname'],
                            lastname=flask.request.form['lastname'])
        return flask.redirect(flask.url_for('index'))
