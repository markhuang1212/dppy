import sys
import math
import numpy as np

import utils
from dp_median import DpMedian

class DpMedianSmoothSensitivity(DpMedian):

    def __init__(self, epsilon: float, U=(1 << 32)-1):
        super().__init__(epsilon, U)

    def computeJs(self, data: list[int], s: int, t: int, L: int, R: int) -> list[int]:
        if s > t:
            return []
        m = (s+t)//2
        idx = -1
        tmp = float('-inf')
        for i in range(L, R+1):
            v = (data[i] - data[m]) * math.exp(-self.epsilon * (i - m))
            if(v > tmp):
                tmp = v
                idx = i
        assert idx != -1
        return self.computeJs(data, s, m-1, L, idx) + [idx] + self.computeJs(data, m+1, t, idx, R)

    def smoothSensitivity(self, data: list[int]) -> float:
        n = len(data)
        js = self.computeJs(data, 0, n//2, n//2, n-1)
        ret = 0.0
        for i in range(0, n//2+1):
            j = js[i]
            assert j >= n//2
            v = (data[j]-data[i])*math.exp(-self.epsilon*(j - i))
            if v > ret:
                ret = v
        return ret

    def smoothSensitibityBruteForce(self, data: list[int]) -> float:
        n = len(data)
        m = n//2
        ret = 0.0
        for k in range(0, n+1):
            for t in range(0, k+1):
                if m+t < n and m+t-k >= 0:
                    j = m+t
                    i = m+t-k
                    assert i <= n//2
                    assert j >= n//2
                    v = (data[j]-data[i]) * math.exp(- k * self.epsilon)
                    if v > ret:
                        ret = v
        return ret

    def answer(self, data: list[int]) -> int:
        ss = self.smoothSensitivity(data)
        # ss = self.smoothSensitibityBruteForce(data)
        med = utils.compute_median(data)
        noise = np.random.normal(0, ss/self.epsilon)
        return int(med + noise)
