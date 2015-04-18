#!/usr/bin/env python

from flask import render_template, make_response, Blueprint
from flask.ext import restful
from flask.ext.restful import Api

api = Blueprint("root", __name__, template_folder="templates")

rest = Api(api)


class IndexPage(restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


class LoginRegister(restful.Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

    def post(self):
        # TODO: login the user
        return "logging in"

    def put(self):
        # TODO: register the user
        return "register"


rest.add_resource(IndexPage, '/')
rest.add_resource(LoginRegister, '/login')
