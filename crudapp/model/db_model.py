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

import database.database as database
from database.data_models import Person

database.init_db()
session = database.db_session


def all_people():
    q = Person.query.all()
    return q


def add_person(firstname, lastname):
    np = Person(firstname=firstname,  lastname=lastname)
    session.add(np)
    session.commit()
    return True


def delete_person(person_id):
    p = session.query(Person).filter_by(
        person_id=person_id
    ).one()
    session.delete(p)
    session.commit()
    return True


def edit_person(person_id, firstname, lastname):
    p = session.query(Person).filter_by(
        person_id=person_id
    ).one()
    p.lastname = lastname
    p.firstname = firstname
    session.commit()
    return True
