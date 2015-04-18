#!/usr/bin/env python

from flask.ext.restful import Resource
from models.charity import Charity as C


class Charity(Resource):
    def get(self, charity_name):
        return "{}".format(charity_name)


class Charities(Resource):
    def get(self):

        charities = C.query.all()
        return charities
