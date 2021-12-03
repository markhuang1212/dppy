import math
import random
from bisect import bisect_right
from dp_median import DpMedian


class DpMedianInverseSensitivity(DpMedian):
    """
    Use Inverse Sensitivity Method (aka exponential mechanism) to answer median query
    """

    def __init__(self, epsilon: float, U=(1 << 32)-1):
        super().__init__(epsilon, U)

    class Interval:
        def __init__(self, start: int, end: int, length: int, prob: float = 0.0):
            self.start = start
            self.end = end
            self.len = length
            self.prob = prob

    def answer(self, data: list[int]) -> int:
        n = len(data)
        mid_idx = n // 2
        len_tmp = -mid_idx  # inverse sensitivity
        intervals: list[self.Interval] = []
        intervals.append(self.Interval(0, data[0]-1, -len_tmp))
        len_tmp += 1
        for i in range(0, mid_idx):
            intervals.append(self.Interval(data[i], data[i+1], -len_tmp))
            len_tmp += 1
        intervals.append(self.Interval(data[mid_idx], data[mid_idx], 0))
        len_tmp += 1
        for i in range(mid_idx, n-1):
            intervals.append(self.Interval(data[i]+1, data[i+1], len_tmp))
            len_tmp += 1
        intervals.append(self.Interval(data[n-1]+1, self.U, len_tmp))
        len_tmp += 1
        for i in range(0, len(intervals)):
            intervals[i].prob = math.exp(-intervals[i].len *
                                         self.epsilon / 2.0)
        intervals = list(filter(lambda x: x.start <= x.end, intervals))
        probability_accu: list[float] = [None] * len(intervals)
        probability_accu[0] = intervals[0].prob
        for i in range(1, len(intervals)):
            probability_accu[i] = probability_accu[i-1] + intervals[i].prob
        rand_val = random.random() * probability_accu[-1]
        idx = bisect_right(probability_accu, rand_val)
        assert intervals[idx].start <= intervals[idx].end
        ret = random.randint(intervals[idx].start, intervals[idx].end)
        return ret
