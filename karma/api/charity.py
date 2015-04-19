#!/usr/bin/env python

import json
from flask import request
from flask.ext.restful import Resource
from models.charity import Charity as C
from karma import db
from karma.models import User
from karma.api import profile


def create_response(charity, recursing=False):
    if recursing:
        return {
            "id": charity.id,
            "name": charity.name,
            "charity": True,
            "description": charity.description}
    return {
        "id": charity.id,
        "name": charity.name,
        "description": charity.description,
        "charity": True,
        "followers": map(lambda x: profile.create_response(x, recursing=True), charity.followers)
    }


class Charity(Resource):
    def get(self, charity_name):
        c = C.query.filter_by(id=charity_name).first_or_404()

        return create_response(c)

    def put(self, charity_name):
        try:
            obj = json.loads(request.data)
        except ValueError:
            return {"status": 400}
        user = User.query.get_or_404(obj['user'])
        charity = C.query.get_or_404(charity_name)
        if charity in user.following_charities:
            return {"status": 400}

        user.following_charities.append(charity)
        db.session.add(user)
        db.session.commit()

        return create_response(charity)


class Charities(Resource):
    def get(self):

        charities = C.query.all()
        ret = list()

        for charity in charities:
            ret.append(create_response(charity))
        ret.reverse()
        return {"data": ret}


class TopCharity(Resource):
    def get(self):

        charities = C.query.all()

        s_charities = list()
        for charity in charities:
            s_charities.append(
                (len(charity.followers), charity)
            )
        s_charities.sort(reverse=True)
        return {"data": map(lambda x: create_response(x[1]), s_charities)}
