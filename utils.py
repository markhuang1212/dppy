"""
Utility Functions
"""

from bisect import bisect_left, bisect_right


def compute_median(data: list[int]) -> int:
    """
    Computes the median of a list of numbers
    """
    return data[(len(data) - 1) // 2]


def rank_error_signed(data: list[int], x: int) -> int:
    """
    Computes the signed rank error of a list of numbers
    """
    med = compute_median(data)
    if x == med:
        return 0
    elif x < med:
        idx = bisect_right(data, x)
        return idx - 1 - len(data)//2
    else:
        idx = bisect_left(data, x)
        return idx - len(data)//2


def rank_error(data: list[int], x: int) -> int:
    """
    Computes the rank error of a list of numbers
    """
    return abs(rank_error_signed(data, x))

def absolute_error(data: list[int], x: int) -> int:
    """
    Computes the absolute error of a list of numbers
    """
    return abs(x - compute_median(data))
    