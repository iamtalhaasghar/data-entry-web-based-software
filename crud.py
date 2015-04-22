#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import os

import crudapp.controller.main_controller as controller

# set folder for static data
PWD = os.environ.get("PWD")

template_folder = os.path.join(PWD, "crudapp/view/templates")
static_folder = os.path.join(PWD, "crudapp/view/static")

app = flask.Flask(__name__,
                  template_folder=template_folder,
                  static_folder=static_folder)

controller.def_control(app)

app.run(debug=True)
