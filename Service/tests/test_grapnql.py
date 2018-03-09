''' Flask integration test '''
from unittest import TestCase
from routes import routes

class TestRoutes(TestCase):
    def test_graphql_for_person_by_id(self):
        import json
        expected_response = '{"data":{"person":{"name":"Jack"}}}'
        with routes.my_service.test_client() as client:
            response = client.get('/graphql?query=query something{person(id:1){name}}')
            assert json.loads(response.data) == json.loads(expected_response)

    def test_graphql_for_all_person(self):
        import json
        with routes.my_service.test_client() as client:
            response = client.get("/graphql?query=query something{persons{id\nname}}")
            print(response.data)
            assert 2 ==  len(json.loads(response.data)["data"]["persons"])