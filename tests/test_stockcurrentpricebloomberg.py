from unittest import TestCase
from StockPortfolio import stockcurrentpricebloomberg
import requests


class TestStockcurrentpricebloomberg(TestCase):
    def test_stockcurrentprice(self):
        response = requests.get('https://www.bloomberg.com')
        assert response.content


class TestStockcurrentpricebloomberg(TestCase):
    def test_stockcurrentprice(self):
        self.assertNotEqual(stockcurrentpricebloomberg('https://www.bloomberg.com/quote/AXY:CN'), None)
