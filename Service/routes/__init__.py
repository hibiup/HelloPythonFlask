''' MicroServices for Hello World functions '''

__version__="0.0.1"

from flask import Flask, Response, jsonify
import json

class JSONResponse(Response):
    def __init__(self, response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False):
        if isinstance(response, (str, bytes, bytearray)):
            response = json.dumps( {'Content' : response} )
            mimetype = 'application/json'
        return super(JSONResponse, self).__init__(response=response, status=status, headers=headers, mimetype=mimetype, content_type=content_type, direct_passthrough=direct_passthrough)

    @classmethod
    def force_type(cls, response, environ=None):
        response = jsonify( {'Content' : response} )
        return super(JSONResponse, cls).force_type(response, environ)

''' 定义 flash app 入口 '''
my_service = Flask(__name__)
my_service.response_class=JSONResponse