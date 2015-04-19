#!/usr/bin/env python

from karma import db


karma_posts = db.Table('karma_posts', db.Model.metadata,
                       db.Column('left_id',
                                 db.Integer, db.ForeignKey('user.id'), primary_key=True),
                       db.Column('right_id',
                                 db.Integer, db.ForeignKey('post.id'), primary_key=True))
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), index=True)
    content = db.Column(db.String(1000), index=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    karma = db.relationship('User',
                            secondary=karma_posts,
                            backref='liked_posts')
