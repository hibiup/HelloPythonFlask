from ..domain import hello
from flask import Flask
from ..utils.serdes import JSONResponse

"""
Flask 原生接口。
"""


''' 定义 flash app 入口 '''
my_service = Flask(__name__)
my_service.response_class = JSONResponse


''' Service routers '''
@my_service.route('/<string:username>', methods=['GET', 'POST'])
@my_service.route('/hello/<string:username>', methods=['GET', 'POST'])
def index(username):
    return hello.greeting(username)
