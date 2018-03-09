import json
from flask import Flask, Response, jsonify, request

from graphqls import PersonQueries
from flask_graphql import GraphQLView

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
my_service.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=PersonQueries.schema, graphiql=True))
#my_service.response_class=JSONResponse