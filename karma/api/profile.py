#!/usr/bin/env

from flask.ext.restful import Resource
from karma.models import User


class Profile(Resource):

    def get(self, profile_id):
        user = User.query.get_or_404(profile_id)

        return {
            "id": user.id,
            "username": user.username,
            "following": user.following}


class Profiles(Resource):

    def get(self):
        users = User.query.all()
        ret = list()

        for user in users:
            ret.append({
                "id": user.id,
                "username": user.username,
                "following": user.following})

        ret.reverse
        return {"data": ret}
