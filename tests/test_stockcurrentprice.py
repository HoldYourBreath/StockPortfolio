from unittest import TestCase
from StockPortfolio import stockcurrentprice
import requests


class TestStockcurrentprice(TestCase):
    def test_stockcurrentprice(self):
        response = requests.get('https://www.bloomberg.com')
        assert response.content


class TestStockcurrentprice(TestCase):
    def test_stockcurrentprice(self):
        self.assertNotEqual(stockcurrentprice('https://www.bloomberg.com/quote/AXY:CN'), None)
