from unittest import TestCase
from StockPortfolio import ranking_list

class TestRanking_list(TestCase):
    def test_ranking_list(self):
        list = [20, 10, 6.4, 5.2, 10000, 5000]
        self.assertTrue(ranking_list(list), [5.2, 6.4, 10, 20, 5000, 10000])
