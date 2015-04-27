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

import crudapp.model.data_store as dstore
# dstore: Data store
from sqlalchemy.exc import IntegrityError as sqla_IntegrityError

def def_control(app):

    # This is part of the data storage initialization
    dstore.teardown(app)

    @app.route('/')
    def index():
        q = dstore.query_all_people()
        print flask.url_for('static', filename='index.html')
        # Returns main page
        return flask.render_template('index.html', people=q)

    # The data that comes from a method POST is stored by flask in
    # request.form
    @app.route('/add_person', methods=['POST'])
    def add_person():
        dstore.add_person(flask.request.form['firstname'],
                          flask.request.form['lastname'])
        # Returns a 300 redirection command with the the url corresponding
        # to function index(). Then the browser will ask for that url.
        return flask.redirect(flask.url_for('index'))

    @app.route('/delete_person', methods=['POST'])
    def delete_person():
        dstore.delete_person(flask.request.form['person_id'])

        return flask.redirect(flask.url_for('index'))

    @app.route('/edit_person', methods=['POST'])
    def edit_person():
        dstore.edit_person(flask.request.form['person_id'],
                           flask.request.form['firstname'],
                           flask.request.form['lastname'])
        return flask.redirect(flask.url_for('index'))

    @app.errorhandler(404)
    def page_not_found(error):
        return flask.render_template('page_not_found.html'), 404

    # @app.errorhandler(flask.DatabaseError)
    # def special_exception_handler(error):
    #     return 'Database connection failed', 500

    @app.errorhandler(sqla_IntegrityError)
    def special_exception_handler(error_msg):
        msg = 'Error: Last names must be unique'
        return flask.render_template('server_error.html', msg=msg), 500

    @app.errorhandler(AssertionError)
    def special_exception_handler(error_msg):
        return flask.render_template('server_error.html', msg=error_msg), 500

