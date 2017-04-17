from unittest import TestCase
from StockPortfolio import investmentpercentage


class TestStockpercentage(TestCase):
    def test_investmentpercentage(self):
        self.assertEqual(investmentpercentage(5,10), 50)
