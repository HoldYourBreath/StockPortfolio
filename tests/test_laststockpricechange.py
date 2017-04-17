from unittest import TestCase
from StockPortfolio import laststockpricechange

class TestLaststockpricechange(TestCase):
    def test_laststockpricechange(self):
        self.assertEqual(laststockpricechange(1, 0.5), -50)







