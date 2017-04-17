from unittest import TestCase
import requests

class TestLaststockpricechange(TestCase):
    def test_previousstockclose(self):
        response = requests.get('https://www.bloomberg.com')
        assert response.content
