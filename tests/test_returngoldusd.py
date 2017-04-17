from unittest import TestCase
from StockPortfolio import returngoldusd
import requests

class TestReturngoldusd(TestCase):
    def test_returngoldusd(self):
        response = requests.get('https://bors-nliv.svd.se/')
        assert response.content


class TestReturngoldusd(TestCase):
    def test_returngoldusd(self):
        self.assertNotEqual(returngoldusd(), None)
