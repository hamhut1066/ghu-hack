#!/usr/bin/env python


from flask import Blueprint

from flask.ext.restful import Api


api = Blueprint("api", __name__, template_folder="templates")

rest = Api(api)

from karma.api.charity import Charity, Charities
from karma.api.post import Post, Posts
from karma.api.profile import Profile, Profiles, Feed, Top

# Adding resources
rest.add_resource(Charity, '/charities/<int:charity_name>')
rest.add_resource(Charities, '/charities/')
rest.add_resource(Post, '/posts/<int:post_id>')
rest.add_resource(Posts, '/posts/')
rest.add_resource(Feed, '/profiles/<int:profile_id>/feed')
rest.add_resource(Top, '/profiles/top')
rest.add_resource(Profile, '/profiles/<int:profile_id>')
rest.add_resource(Profiles, '/profiles/')
