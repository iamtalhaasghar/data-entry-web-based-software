#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask

import crudapp.model.curl_model as curl_model


def def_control(app):

    @app.before_request
    def before():
        curl_model.print_incoming_request(flask.request)

    @app.after_request
    def after(response):
        curl_model.print_outgoing_response(response)
        return response
