''' Flask integration test '''

from unittest import TestCase
from routes import routes
#from routes import my_service
from .test_hello import __random_string__
import re

class TestRoutes(TestCase):
    ''' Test service routes '''
    def test_moke_greeting_rest(self):
        ''' Test hello rest service '''
        with routes.my_service.test_client() as client:
            username = __random_string__()

            resp = client.get('/hello/' + username)
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Hello, " + username + "!", str(resp.data)))

            resp = client.post('/hello/' + username)
            resp = routes.my_service.make_response(resp)
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Hello, " + username + "!", str(resp.data)))
