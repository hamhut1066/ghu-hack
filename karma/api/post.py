#!/usr/bin/env python

from flask import request
import json
from flask.ext.login import current_user
from flask.ext.restful import Resource
from karma.api.models.post import Post as P


class Post(Resource):
    def get(self, post_id):
        p = P.query.filter_by(id=post_id).first_or_404()

        return {
            "id": p.id,
            "title": p.title,
            "content": p.content,
            "user_id": p.user_id}


class Posts(Resource):
    def get(self):

        posts = P.query.all()
        ret = list()

        for post in posts:
            ret.append({
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "user_id": post.user_id
            })
        return {"data": ret}

    def put(self):
        try:
            obj = json.loads(request.data)
        except ValueError:
            return {"status": 400}
        
