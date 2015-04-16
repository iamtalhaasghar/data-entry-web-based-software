#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy as sqa
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dcl

import database


class Person(database.Base):
    __tablename__ = 'People'
    # __table_args__ = (sqa.Index("index-users", 'name',
    #                             'fullname', unique=True), )
    person_id = sqa.Column(sqa.Integer,
                           sqa.Sequence('person_id_seq'),
                           primary_key=True)

    firstname = sqa.Column(sqa.String(50, convert_unicode=True),
                           nullable=False, index=True)

    lastname = sqa.Column(sqa.String(50, convert_unicode=True),
                          nullable=False, index=True, unique=True)

    def __repr__(self):
        return self.__unicode__().encode('utf-8')

    def __unicode__(self):
        return u"<People(firstname={}, lastname={})>".format(self.firstname,
                                                             self.lastname)
