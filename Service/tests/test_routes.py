''' Flask integration test '''

from unittest import TestCase
from routes import routes
#from routes import my_service
from .test_hello import __random_string__
import re

class TestRoutes(TestCase):
    ''' Test service routes '''
    
    def test_index(self):
        ''' Test index '''
        with routes.my_service.test_client() as client:
            resp = client.get('/')
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Index", str(resp.data)))


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


    def test_metrics(self):
        with routes.my_service.test_client() as client:
            resp = client.get('/metrics')
            self.assertEqual(200, resp.status_code)
            self.assertTrue(resp.content_type.startswith('text/plain'))
            self.assertIsNotNone(re.search("request_latency_seconds", str(resp.data)))
