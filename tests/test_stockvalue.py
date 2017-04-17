from unittest import TestCase
from StockPortfolio import stockvalue


class TestStockcurrentvalue(TestCase):
    def test_stockcurrentvalue(self):
        self.assertEqual(stockvalue(3,4,2), 24)