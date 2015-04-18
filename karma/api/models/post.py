#!/usr/bin/env python

from karma import db


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    content = db.Column(db.String(1000), index=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
