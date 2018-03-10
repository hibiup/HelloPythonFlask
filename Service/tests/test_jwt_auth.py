from unittest import TestCase
from routes import routes
import json

class TestRoutes(TestCase):
    @classmethod
    def post_json(cls, client, url, data):
        data = json.dumps(data)
        resp = client.post(url, headers={'Content-Type': 'application/json'}, data=data)
        print(resp.data)
        return resp, json.loads(resp.data)

    def test_auth_endpoint_with_valid_request(self):
        with routes.my_service.test_client() as client:
            resp, jdata = TestRoutes.post_json(
                client, '/auth', {'username': 'user1', 'password': 'abcxyz'})
            assert resp.status_code == 200
            assert 'access_token' in jdata

    def test_access_protected_endpoint(self):
        with routes.my_service.test_client() as client:
            resp, jdata = TestRoutes.post_json(
                client, '/auth', {'username': 'user1', 'password': 'abcxyz'})
            token = jdata['access_token']

            resp = client.get('/protected', headers={'Authorization': 'JWT ' + token})
            print(resp.data )
            assert resp.status_code == 200
            assert resp.data == b'User(id=\'1\')'

    def test_access_protected_endpoint_without_auth(self):
        with routes.my_service.test_client() as client:
            resp = client.get('/protected')
            assert resp.status_code == 401