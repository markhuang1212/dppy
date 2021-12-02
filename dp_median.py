"""
Base class for median computation
"""

from abc import ABC, abstractmethod


class DpMedian(ABC):
    """
    Base class for median computation
    """

    def __init__(self, U=(1 << 32)-1):
        self.U = U

    @abstractmethod
    def answer(self, data: list[int]) -> int:
        """
        return answer
        """
