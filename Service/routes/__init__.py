''' MicroServices for Hello World functions '''

__version__="0.0.1"

from routes import routes

def start():
    ''' 定义 flash app 入口 '''
    routes.my_service.run()