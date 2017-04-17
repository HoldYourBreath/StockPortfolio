from unittest import TestCase
from StockPortfolio import stock_buy


class TestStock_buy(TestCase):
    def test_stock_buy(self):
        self.assertTrue(stock_buy(20, 10, 3.4, 5.2, 10000, 5000), True)


class TestStock_buy(TestCase):
    def test_stock_buy(self):
        self.assertFalse(stock_buy(20, 30, 3.4, 5.2, 10000, 5000), False)

class TestStock_buy(TestCase):
    def test_stock_buy(self):
        self.assertFalse(stock_buy(20, 10, 6.4, 5.2, 10000, 5000), False)

class TestStock_buy(TestCase):
    def test_stock_buy(self):
        self.assertFalse(stock_buy(20, 10, 2.4, 5.2, 10000, 50000), False)

class TestStock_buy(TestCase):
    def test_stock_buy(self):
        self.assertFalse(stock_buy(20, 5, 2.4, 2.4, 10000, 2000), False)
