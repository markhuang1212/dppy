"""
Base class for median computation
"""

from abc import ABC, abstractmethod


class DpMedian(ABC):
    """
    Base class for median computation
    """

    def __init__(self, epsilon: float,  U: int):
        self.U = U
        self.epsilon = epsilon

    @abstractmethod
    def answer(self, data: list[int]) -> int:
        """
        return answer
        """
