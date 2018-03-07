#from routes import my_service
from domain import hello
from flask import request
import json

from flask import Flask, Response, jsonify

class JSONResponse(Response):
    def __init__(self, response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False):
        if isinstance(response, (str, bytes, bytearray)):
            response = json.dumps( {'Content' : response} )
            mimetype = 'application/json'
        return super(JSONResponse, self).__init__(response=response, status=status, headers=headers, mimetype=mimetype, content_type=content_type, direct_passthrough=direct_passthrough)

    @classmethod
    def force_type(cls, response, environ=None):
        if(200 == response.code):
            response = jsonify( {'Content' : response} )
        return super(JSONResponse, cls).force_type(response, environ)

my_service = Flask(__name__)
my_service.response_class=JSONResponse

@my_service.route('/', methods=['GET', 'POST'])
def index():
    return "Index"

@my_service.route('/hello/<username>', methods=['GET', 'POST'])
def greeting(username):
    return hello.greeting(username)
