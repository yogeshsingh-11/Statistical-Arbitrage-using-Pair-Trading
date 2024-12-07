import unittest
import pandas as pd
from src.pair_trading import generate_signals, backtest_pair_trading

class TestPairTrading(unittest.TestCase):

    def test_generate_signals(self):
        spread = pd.Series([1, 2, 3, 4, 5, 6, 7])
        signals = generate_signals(spread)
        self.assertEqual(signals['signal'].iloc[0], 0)  # No signal at the start

    def test_backtest_pair_trading(self):
        asset1 = pd.Series([100, 101, 102, 103, 104, 105, 106])
        asset2 = pd.Series([95, 96, 97, 98, 99, 100, 101])
        results = backtest_pair_trading(asset1, asset2)
        self.assertEqual(results['strategy_returns'].iloc[0], 0)  # No strategy return at the start

if __name__ == "__main__":
    unittest.main()

