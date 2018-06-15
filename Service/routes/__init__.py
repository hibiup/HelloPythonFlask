''' MicroServices for Hello World functions '''

__version__="0.0.1"

from .routes import my_service

def start():
    my_service.run(host='0.0.0.0')