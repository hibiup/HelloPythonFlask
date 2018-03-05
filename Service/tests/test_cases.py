from unittest import TestCase


import hello

class TestJoke(TestCase):
    def test_hello(self):
        hello.greeting()
