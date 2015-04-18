#!/usr/bin/env python

from karma import db


class Charity(db.Model):
    __tablename__ = 'charity'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), index=True)
    description = db.Column(db.String(1000), index=False)
