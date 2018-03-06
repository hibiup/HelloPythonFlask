from . import my_service
from domain import hello
from flask import request
import json

@my_service.route('/<string:username>', methods=['GET', 'POST'])
@my_service.route('/hello/<string:username>', methods=['GET', 'POST'])
def index(username):
    return hello.greeting(username)