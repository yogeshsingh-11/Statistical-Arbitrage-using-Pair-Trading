import unittest
import pandas as pd
from src.cointegration import test_cointegration

class TestCointegration(unittest.TestCase):

    def test_cointegration(self):
        asset1 = pd.Series([100, 101, 102, 103, 104, 105, 106])
        asset2 = pd.Series([95, 96, 97, 98, 99, 100, 101])
        self.assertTrue(test_cointegration(asset1, asset2))  # Should return True for cointegration

if __name__ == "__main__":
    unittest.main()

