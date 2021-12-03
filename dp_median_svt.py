import numpy as np
from bisect import bisect_right
from dp_median import DpMedian


class DpMedianSvt(DpMedian):
    def __init__(self, epsilon: float, U: int = 10**6):
        super().__init__(epsilon, U)

    def count(self, data: list[int], target: int) -> float:
        return np.random.laplace(0, 4.0/self.epsilon) + bisect_right(data, target)

    def getT(self, N: int) -> float:
        return np.random.laplace(0, 2.0/self.epsilon) + N//2

    def answer(self, data: list[int]) -> int:
        T = self.getT(len(data))
        for i in range(self.U):
            if self.count(data, i) >= T:
                return i
