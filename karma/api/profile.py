#!/usr/bin/env

from flask import request
import json
from flask.ext.restful import Resource
from karma.models import User
from karma.api.models.post import Post
from karma.api import post
from karma import db


def create_response(user, recursing=False):
    from karma.api import charity, post
    if recursing:
        return {
            "id": user.id,
            # "description": user.description,
            "username": user.username}
    return {
        "id": user.id,
        "username": user.username,
        # "description": user.description,
        "liked_posts": map(lambda x: post.create_response(x, recursing=True), user.liked_posts),
        "following_users": map(lambda x: create_response(x, recursing=True), user.following_users),
        "followers": map(lambda x: create_response(x, recursing=True), user.followers),
        "following_charities": map(lambda x: charity.create_response(x, recursing=True), user.following_charities)}


class Profile(Resource):

    def get(self, profile_id):
        user = User.query.get_or_404(profile_id)

        return create_response(user)

    def put(self, profile_id):
        # add following to this user
        try:
            obj = json.loads(request.data)
        except ValueError:
            return {"status": 400}

        user = User.query.get_or_404(profile_id)
        current_user = User.query.get_or_404(obj['user'])
        current_user.following_users.append(user)
        db.session.add(current_user)
        db.session.commit()

        return create_response(current_user)


class Profiles(Resource):

    def get(self):
        users = User.query.all()
        ret = list()

        for user in users:
            ret.append(create_response(user))

        ret.reverse
        return {"data": ret}


class Feed(Resource):
    def get(self, profile_id):
        user = User.query.get_or_404(profile_id)

        try:
            your_posts = Post.query.filter_by(user_id=user.id)
            following_users_post = list()
            for _user in user.following_users:
                if _user == user:
                    continue
                following_users_post += Post.query.filter_by(user_id=_user.id)
            return {
                "data": {
                    "posts": map(lambda x: post.create_response(x), your_posts),
                    "following_posts": map(lambda x: post.create_response(x), following_users_post)
                }
            }
        except Exception:
            raise
            return {"status": 400}
