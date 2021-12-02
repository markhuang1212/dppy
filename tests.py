"""
Unit Testing
"""

import unittest

import random

from utils import compute_median, rank_error
from dp_median_binary_search import DpMedianBinarySearch
from dp_median_smooth_sensitivity import DpMedianSmoothSensitivity


class TestMedianUtil(unittest.TestCase):
    """
    Unit Testing
    """

    def test_median(self):
        """
        Test true median
        """
        self.assertEqual(compute_median([1, 3, 5, 7, 9]), 5)
        self.assertEqual(compute_median([1, 3, 5, 7]), 5)
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
        self.assertEqual(rank_error([1, 3, 5, 7], 0), 3)
        self.assertEqual(rank_error([1, 3, 5, 7], 1), 2)

    def test_dp_median(self):
        """
        Test DP Median Binary Search
        """
        data = []
        for i in range(1, 1000):
            data.append(i*10)
        ans = DpMedianBinarySearch(0.1).answer(data)
        ans = DpMedianSmoothSensitivity(0.1).answer(data)

    def test_Js(self):
        dpss = DpMedianSmoothSensitivity(0.1)
        data = []
        for _ in range(10):
            data.append(random.randint(1, 10000))
        data.sort()
        print(dpss.smoothSensitivity(data))
        print(dpss.smoothSensitibityBruteForce(data))


if __name__ == '__main__':
    unittest.main()
