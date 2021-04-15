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
    if username == 'admin@email.com' and password == 'secret':
        return True
    else:
        return False
