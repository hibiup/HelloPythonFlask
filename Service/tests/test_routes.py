''' Flask integration test '''

from unittest import TestCase
from routes import my_service
from .test_hello import __random_string__

class TestRoutes(TestCase):
    ''' Test service routes '''
    def test_moke_greeting_rest(self):
        ''' Test hello rest service '''
        import re
        with my_service.test_client() as client:
            username = __random_string__()

            resp = client.get('/' + username)
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Hello, " + username + "!", str(resp.data)))

            resp = client.get('/hello/' + username)
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Hello, " + username + "!", str(resp.data)))

            resp = client.post('/hello/' + username)
            resp = my_service.make_response(resp)
            print(resp.data)
            self.assertEqual(200, resp.status_code)
            self.assertIsNotNone(re.search("Hello, " + username + "!", str(resp.data)))
