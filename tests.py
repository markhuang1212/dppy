"""
Unit Testing
"""

import unittest

from utils import compute_median, rank_error
from dp_median_binary_search import DpMedianBinarySearch


class TestMedianUtil(unittest.TestCase):
    """
    Unit Testing
    """

    def test_median(self):
        """
        Test true median
        """
        self.assertEqual(compute_median([1, 3, 5, 7, 9]), 5)
        self.assertEqual(compute_median([1, 3, 5, 7]), 3)
        self.assertEqual(compute_median([1]), 1)

    def test_rank_error(self):
        """
        Test rank error
        """
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 0), 3)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 1), 2)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 2), 2)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 3), 1)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 4), 1)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 5), 0)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 6), 1)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 7), 1)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 8), 2)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 9), 2)
        self.assertEqual(rank_error([1, 3, 5, 7, 9], 10), 3)

    def test_dp_median_binary_search(self):
        """
        Test DP Median Binary Search
        """
        data = []
        for i in range(1, 10000):
            data.append(i*10)
        ans = DpMedianBinarySearch(0.1).answer(data)
        print(rank_error(data, ans))


if __name__ == '__main__':
    unittest.main()
