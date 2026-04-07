# src/stat_engine.py

import math
from typing import List, Union

class StatEngine:
    """
    A simple statistical engine to process 1D numerical data.
    Handles mean, median, mode, variance, standard deviation, and outlier detection.
    """

    def __init__(self, data):
        # Check empty list
        if not data:
            raise ValueError("Data list cannot be empty.")

        # Check for non-numeric values
        for i, value in enumerate(data):
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Invalid data at index {i}: {value}. All values must be numeric."
                )

        # Store clean data
        self.data = list(data)

    # ------------------ Central Tendency ------------------

    def get_mean(self) -> float:
        return sum(self.data) / len(self.data)

    def get_median(self) -> float:
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def get_mode(self) -> Union[float, List[float], str]:
        frequency = {}
        for num in self.data:
            frequency[num] = frequency.get(num, 0) + 1

        max_count = max(frequency.values())

        if max_count == 1:
            return "All values are unique, no mode."

        modes = [k for k, v in frequency.items() if v == max_count]
        return modes if len(modes) > 1 else modes[0]

    # ------------------ Dispersion ------------------

    def get_variance(self, is_sample: bool = True) -> float:
        n = len(self.data)
        mean = self.get_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]

        if is_sample:
            if n < 2:
                raise ValueError("Sample variance requires at least 2 data points.")
            return sum(squared_diff) / (n - 1)
        else:
            return sum(squared_diff) / n

    def get_standard_deviation(self, is_sample: bool = True) -> float:
        return math.sqrt(self.get_variance(is_sample))

    # ------------------ Outlier Detection ------------------

    def get_outliers(self, threshold: float = 2) -> List[float]:
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()
        return [x for x in self.data if abs(x - mean) > threshold * std_dev]