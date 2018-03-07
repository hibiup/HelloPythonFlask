#from routes import my_service
from domain import hello
from routes.ws_server import my_service

from routes import metrics

@my_service.route('/', methods=['GET', 'POST'])
def index():
    return "Index"

@my_service.route('/hello/<username>', methods=['GET', 'POST'])
def greeting(username):
    return hello.greeting(username)
