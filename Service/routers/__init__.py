''' MicroServices for Hello World functions '''

__version__="0.0.1"

from .routers import my_service

my_service.run(host='0.0.0.0')