#!/usr/bin/env python

from flask import Flask
from views import IndexPage, LoginRegister
from flask.ext.sqlalchemy import SQLAlchemy


# TODO: setup sqlalchemy
app = Flask(__name__)
db = SQLAlchemy(app)


from karma.api import api

app.register_blueprint(api, url_prefix="/api")

from karma.views import api

app.register_blueprint(api, url_prefix="")



if __name__ == '__main__':
        app.run(debug=True)
