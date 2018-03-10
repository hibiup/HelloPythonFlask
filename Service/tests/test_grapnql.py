''' Flask integration test '''
from unittest import TestCase
from routes import routes

class TestRoutes(TestCase):
    def test_graphql_for_person_by_id(self):
        import json
        expected_response = '{"data":{"person":{"name":"Jack"}}}'
        with routes.my_service.test_client() as client:
            response = client.get('/graphql?query=query something{ person(id:1){ name }}')
            assert json.loads(response.data) == json.loads(expected_response)

    def test_graphql_for_all_persons(self):
        import json
        with routes.my_service.test_client() as client:
            response = client.get("/graphql?query=query something{ persons{ id\nname }}")
            print(response.data)
            assert 3 ==  len(json.loads(response.data)["data"]["persons"])

    def test_graphql_for_persons_with_condition(self):
        import json
        with routes.my_service.test_client() as client:
            response = client.get("/graphql?query=query something{ personsWithCondition(age:34){ id\nname\nage } }")
            print(response.data)
            assert 2 ==  len(json.loads(response.data)["data"]["personsWithCondition"])
    
    def test_graphql_for_person_creation(self):
        import json
        expected_response = '{"data":{"createPerson":{"id":4,"name":"Newbeen","age":1.0}}}'
        with routes.my_service.test_client() as client:
            response = client.post("/graphql?query=mutation { createPerson(name: \"Newbeen\", age: 1, avatar: \"\"){ id\nname\nage } }")
            print(response.data)
            assert json.loads(response.data) == json.loads(expected_response)

    def test_graphql_person_creation_with_invalid_method(self):
        expected_response = 'Can only perform a mutation operation from a POST request.'
        with routes.my_service.test_client() as client:
            response = client.get("/graphql?query=mutation { createPerson(name: \"Newbeen\", age: 1, avatar: \"\"){ id\nname\nage } }")
            print(response.data)
            assert str(response.data).__contains__(expected_response)

    def test_graphql_person_creation_with_invalid_age(self):
        expected_response = 'Invalid age!'
        with routes.my_service.test_client() as client:
            response = client.post("/graphql?query=mutation { createPerson(name: \"Newbeen\", age: -1, avatar: \"\"){ id\nname\nage } }")
            print(response.data)
            assert str(response.data).__contains__(expected_response)

    def test_graphql_person_update(self):
        expected_response = '{"data":{"updatePerson":{"id":2,"name":"new name","age":100.0,"avatar":""}}}'
        with routes.my_service.test_client() as client:
            response = client.post("/graphql?query=mutation { updatePerson(id: 1, name: \"new name\", age: 100, avatar: \"\"){ id\nname\nage\navatar } }")
            print(response.data)
            assert str(response.data).__contains__(expected_response)