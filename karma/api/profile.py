#!/usr/bin/env

from flask import request
import json
from flask.ext.restful import Resource
from karma.models import User
from karma import db


def create_response(user, recursing=False):
    if recursing:
        return {
            "id": user.id,
            "username": user.username}
    return {
        "id": user.id,
        "username": user.username,
        "following_users": map(lambda x: create_response(x, recursing=True), user.following_users),
        "followers": map(lambda x: create_response(x, recursing=True), user.followers),
        "following_charities": user.following_charities}


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
