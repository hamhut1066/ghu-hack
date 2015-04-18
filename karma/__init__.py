#!/usr/bin/env python

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager


# TODO: setup sqlalchemy
app = Flask(__name__)
app.config['SECRET_KEY'] = 'asoenutha.r,scpg23rpuha.sntph3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://moredhel:question@karma.czgce1c04iru.eu-west-1.rds.amazonaws.com:5432/karma'

db = SQLAlchemy(app)
lm = LoginManager(app)


from karma.api import api

app.register_blueprint(api, url_prefix="/api")

from karma.views import api

from karma.models import User

app.register_blueprint(api, url_prefix="")


@lm.user_loader
def load_user(userid):
    return User.query.filter_by(username=userid).first()

if __name__ == '__main__':
        app.run(debug=True)
