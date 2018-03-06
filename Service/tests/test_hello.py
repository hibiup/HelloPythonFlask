''' Unit test cases for hello.py'''

from unittest import TestCase

from domain import hello

def __random_string__(length=5):
    import random, string
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

class TestHello(TestCase):
    def test_greeting(self):
        ''' Test hello.greeting(username) function '''
        import re
        somebody = __random_string__()
        _ = hello.greeting(somebody)
        self.assertIsNotNone(re.search("Hello, " + somebody + "!", _))

