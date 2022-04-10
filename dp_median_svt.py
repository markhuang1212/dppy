import numpy as np
import random
import math
from bisect import bisect_right
from dp_median import DpMedian


class DpMedianSvt(DpMedian):
    def __init__(self, epsilon: float, U: int = 10**6):
        super().__init__(epsilon, U)

    # Given by Dong
    def LapNoise(self):
        a = random.uniform(0, 1)
        b = math.log(1/(1-a))
        c = random.uniform(0, 1)
        if c > 0.5:
            return b
        else:
            return -b

    def count(self, data: list[int], target: int) -> float:
        noise = np.random.laplace(0, 4.0/self.epsilon)
        return noise + bisect_right(data, target)

    def get_t(self, N: int) -> float:
        return np.random.laplace(N//2, 2.0/self.epsilon)

    def answer(self, data: list[int]) -> int:
        T = self.get_t(len(data))
        for i in range(self.U):
            if self.count(data, i) >= T:
                return i
        return self.U
