from unittest import TestCase
from StockPortfolio import stockdifference

class TestStockvalue(TestCase):
    def test_stockdifference(self):
        self.assertEqual(stockdifference(20, 4), 16)
