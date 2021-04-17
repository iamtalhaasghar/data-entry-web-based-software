#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask
import os

import crudapp.controller.main_controller as main_controller
import crudapp.controller.curl_controller as curl_controller

# set folder for static data
PWD = os.getcwd()

template_folder = os.path.join(PWD, "crudapp/view/templates")
static_folder = os.path.join(PWD, "crudapp/view/static")

app = flask.Flask(__name__,
                  template_folder=template_folder,
                  static_folder=static_folder)

main_controller.def_control(app)

# This adds curl-like logging
curl_controller.def_control(app)

if __name__=="__main__":
	app.run(host='0.0.0.0',port=5000)
