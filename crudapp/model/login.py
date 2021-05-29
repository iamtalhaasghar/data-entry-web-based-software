#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" The model receives commands from the controller,
    and interacts with the host computer:
    - reads data from db
    - writes data
    - writes to console
    - logs
    - etc

    The db model is built using SQLAlchemy
"""


def raise_error_if_not_logged_in(session):
    if 'username' not in list(session.keys()):
        raise RuntimeError()

def isUserLoggedIn(session):
    return 'username' in session.keys()

def check_login(username, password):
<<<<<<< HEAD
    if username == 'admin' and password == 'admin' or username == "user" and password == "user":
=======
    if username == 'admin' and password == 'admin':
>>>>>>> da93472469b87cdb17b40f90325a65b13bbce325
        return True
    else:
        return False
