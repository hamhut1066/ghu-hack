#!/usr/bin/env python


from flask import Blueprint

from flask.ext.restful import Api


api = Blueprint("api", __name__, template_folder="templates")

rest = Api(api)

from karma.api.charity import Charity, Charities

# Adding resources
rest.add_resource(Charity, '/charities/<int:charity_name>')
rest.add_resource(Charities, '/charities/')
