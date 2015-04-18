#!/usr/bin/env python

from flask import render_template, make_response, Blueprint, request, abort
from flask.ext import restful
from flask.ext.restful import Api
from flask.ext.login import login_user
import json


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
        from models import User
        # TODO: login the user
        try:
            obj = json.loads(request.data)
        except ValueError:
            abort(400)

        if obj is not None:
            user = User.query.filter_by(username=obj['user']['username']).first_or_404()
            if user.verify_password(obj['user']['password']):
                login_user(user)
                return {"status": "OK"}
        abort(400)


    def put(self):
        # TODO: register the user
        return "register"


rest.add_resource(IndexPage, '/')
rest.add_resource(LoginRegister, '/login')
