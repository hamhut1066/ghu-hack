#!/usr/bin/env python

from flask.ext.restful import Resource


class Charity(Resource):
    def get(self, charity_name):
        return "{}".format(charity_name)
