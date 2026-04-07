# tests/test_stat_engine.py

import unittest
from src.stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def setUp(self):
        self.odd_list = [1, 3, 5]
        self.even_list = [1, 2, 3, 4]
        self.mixed_list = [1, 'a', 3]

    # Test mean calculation
    def test_mean(self):
        engine = StatEngine(self.odd_list)
        self.assertEqual(engine.get_mean(), 3)

    # Test median calculation
    def test_median_odd_even(self):
        engine_odd = StatEngine(self.odd_list)
        engine_even = StatEngine(self.even_list)
        self.assertEqual(engine_odd.get_median(), 3)
        self.assertEqual(engine_even.get_median(), 2.5)

    # Test mode with multiple modes
    def test_mode(self):
        engine = StatEngine([1, 1, 2, 3, 3])
        self.assertEqual(engine.get_mode(), [1, 3])

    def test_standard_deviation(self):
        data = [2, 4, 4, 4, 5, 5, 7, 9]
        engine = StatEngine(data)
        # Known population standard deviation = 2
        self.assertAlmostEqual(engine.get_standard_deviation(is_sample=False), 2.0)

    # Test outlier detection
    def test_outliers(self):
        data = [10, 12, 12, 13, 12, 100]
        engine = StatEngine(data)
        outliers = engine.get_outliers(threshold=2)
        self.assertIn(100, outliers)

    # Test empty list raises ValueError
    def test_empty_data(self):
        with self.assertRaises(ValueError):
            StatEngine([])

    # Test non-numeric data raises TypeError
    def test_mixed_data(self):
        with self.assertRaises(TypeError):
            StatEngine(self.mixed_list)

if __name__ == "__main__":
    unittest.main()