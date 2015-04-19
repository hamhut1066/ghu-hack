#!/usr/bin/env python

from karma.api.models.charity import Charity
from flask.ext.login import UserMixin

from karma import db
from passlib.apps import custom_app_context as pwd_context

association_table = db.Table('association', db.Model.metadata,
                             db.Column('left_id',
                                       db.Integer, db.ForeignKey('user.id'), primary_key=True),
                             db.Column('right_id',
                                       db.Integer, db.ForeignKey('charity.id'), primary_key=True)
                             )
association_table2 = db.Table('association2', db.Model.metadata,
                             db.Column('left_id',
                                       db.Integer, db.ForeignKey('user.id')),
                             db.Column('right_id',
                                       db.Integer, db.ForeignKey('user.id'))
                             )



class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))
    description = db.Column(db.String(1000))
    following_users = db.relationship('User',
                                      secondary=association_table2,
                                      primaryjoin=id==association_table2.c.left_id,
                                      secondaryjoin=id==association_table2.c.right_id,
                                      backref='followers')
    following_charities = db.relationship('Charity',
                                          secondary=association_table,
                                          backref='followers')

    def __init__(self, username=None, description=None, password=None):
        if username:
            self.username = username
        if password:
            self.hash_password(password)
        if description:
            self.description = description

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
