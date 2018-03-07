''' MicroServices for Hello World functions '''

__version__="0.0.1"

from routes import routes

''' 定义 flash app 入口 '''
def start():
    ''' start Flask '''
    routes.my_service.run(host="172.18.0.1")