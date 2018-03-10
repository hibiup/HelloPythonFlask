import json
from flask import Flask, Response, jsonify, request

from graphqls import PersonQueries
from flask_graphql import GraphQLView

@DeprecationWarning
class JSONResponse(Response):
    def __init__(self, response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False):
        if isinstance(response, (str, bytes, bytearray)):
            response = json.dumps( {'Content' : response} )
            mimetype = 'application/json'
        return super(JSONResponse, self).__init__(response=response, status=status, headers=headers, mimetype=mimetype, content_type=content_type, direct_passthrough=direct_passthrough)

    @classmethod
    def force_type(cls, response, environ=None):
        if (200 == response.status_code) and (response.mimetype is None):
            response = jsonify( {'Content' : response} )
        return super(JSONResponse, cls).force_type(response, environ)

my_service = Flask(__name__)
#my_service.response_class=JSONResponse

# 5. Register schema with http server:
my_service.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=PersonQueries.schema, graphiql=True))


# JWT authentication example
# https://pythonhosted.org/Flask-JWT/
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

# Semulate users database
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'password'),
]
username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# 1. Create authenticate method. Identicate user from users database
from werkzeug.security import safe_str_cmp
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

# 2. Create JWT object and assign flask server instance to it.
from flask_jwt import JWT, jwt_required, current_identity
my_service.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(my_service, authenticate, identity)

# 3. Decorate URI by jwt_requested() decorater
@my_service.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# 4. Create client and request JWT from "/auth" endpoint, which is created by default.
# and bring that JWT back in header by "Authentication: JWT ..." to the protected service.
