from unittest import TestCase
#from StockPortfolio import returnexchangerate
import requests

class TestReturnexchangerate(TestCase):
    def test_returnexchangerate(self):
        response = requests.get('http://www.xe.com/sv/')
        assert response.content