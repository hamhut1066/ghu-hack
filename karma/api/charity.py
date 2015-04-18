#!/usr/bin/env python

from flask.ext.restful import Resource
from models.charity import Charity as C


class Charity(Resource):
    def get(self, charity_name):
        c = C.query.filter_by(id=charity_name).first_or_404()

        return {"id": c.id,
                "name": c.name,
                "description": c.description}


class Charities(Resource):
    def get(self):

        charities = C.query.all()
        ret = list()

        for charity in charities:
            ret.append({
                "id": charity.id,
                "name": charity.name,
                "description": charity.description
            })
        return {"data": ret}
