import numpy as np
from dp_median import DpMedian
from bisect import bisect_right
from math import log2


class DpMedianBinarySearch(DpMedian):

    def __init__(self, epsilon: float, U=(1 << 32)-1):
        super().__init__(epsilon, U)
        self.epsilon_op = epsilon / log2(self.U)

    def count(self, data: list[int], target: int) -> float:
        """
        number of i s.t. list[i] <= target
        """
        noise = np.random.normal(0, 0.5/self.epsilon_op)
        # print(noise)
        return noise + bisect_right(data, target)

    def answer(self, data: list[int]) -> int:
        """
        :return: the median of the array
        """
        n = len(data)
        s = 0
        t = self.U
        while s < t:
            mid = (s+t)//2
            if self.count(data, mid) < n / 2:
                s = mid + 1
            else:
                t = mid
        return s
