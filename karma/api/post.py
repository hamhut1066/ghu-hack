#!/usr/bin/env python

from flask import request
import json
from flask.ext.restful import Resource
from karma.api.models.post import Post as P
from karma.models import User
from karma import db


def create_response(p, recursing=False):
    from karma.api import profile
    if recursing:
        return {
            "id": p.id,
            "title": p.title,
            "content": p.content,
            "user_id": p.user_id}
    return {
        "id": p.id,
        "title": p.title,
        "content": p.content,
        "karma": map(lambda x: profile.create_response(x, recursing=True),
                     p.karma),
        "user_id": p.user_id}


class Post(Resource):

    def __init__(self, title=None, content=None, user_id=None):
        if title:
            self.title = title
        if content:
            self.content = content
        if user_id:
            self.user_id = user_id

    def get(self, post_id):
        p = P.query.filter_by(id=post_id).first_or_404()

        return create_response(p)

    def put(self, post_id):
        try:
            obj = json.loads(request.data)
        except ValueError:
            return {"status": 400}
        p = P.query.get_or_404(post_id)
        user = User.query.get(obj['user'])

        p.karma.append(user)
        db.session.add(p)
        db.session.commit()

        return create_response(p)


class Posts(Resource):
    def get(self):

        posts = P.query.all()
        ret = list()

        for post in posts:
            ret.append(create_response(post))
        ret.reverse()
        return {"data": ret}

    def put(self):
        try:
            obj = json.loads(request.data)
            user = User.query.get(obj['user'])
        except ValueError:
            return {"status": 400}

        # create post.
        p = P(title=obj['data']['title'],
                    content=obj['data']['content'],
                    user_id=user.id)

        db.session.add(p)
        db.session.commit()

        return create_response(p)
