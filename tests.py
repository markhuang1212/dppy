"""
Unit Testing
"""

import unittest

import random
from dp_median_inverse_sensitivity import DpMedianInverseSensitivity
from dp_median_svt import DpMedianSvt

from utils import compute_median, rank_error, uniform_rand_array
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
            data.append(i*100)
        ans = DpMedianBinarySearch(0.1).answer(data)
        print("Binary Search", ans)
        ans = DpMedianSmoothSensitivity(0.1).answer(data)
        print("Smooth Sensitivity", ans)
        ans = DpMedianSvt(0.1).answer(data)
        print("SVT", ans)
        ans = DpMedianInverseSensitivity(0.1).answer(data)
        print("Inverse Sensitivity", ans)

    def test_js(self):
        """
        Test the j*(i) function
        """
        dpss = DpMedianSmoothSensitivity(0.1)
        data = uniform_rand_array(1000, 10000)
        # data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
        ss = dpss.smoothSensitivity(data)
        ssbf = dpss.smoothSensitibityBruteForce(data)
        self.assertAlmostEqual(ss, ssbf)


if __name__ == '__main__':
    unittest.main()
