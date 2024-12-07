import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint

def generate_signals(spread, z_score_threshold=2):
    """
    Generate buy and sell signals based on the Z-score of the spread.
    
    :param spread: The spread between two asset prices
    :param z_score_threshold: Threshold for Z-score to trigger signals
    :return: DataFrame with buy/sell signals
    """
    z_score = (spread - spread.mean()) / spread.std()
    signals = pd.DataFrame(index=spread.index)
    signals['z_score'] = z_score
    signals['signal'] = 0
    signals.loc[signals['z_score'] > z_score_threshold, 'signal'] = -1  # Sell
    signals.loc[signals['z_score'] < -z_score_threshold, 'signal'] = 1  # Buy
    return signals

def backtest_pair_trading(price_series1, price_series2, z_score_threshold=2):
    """
    Backtest a pair trading strategy.
    
    :param price_series1: Price series of asset 1
    :param price_series2: Price series of asset 2
    :param z_score_threshold: Threshold for generating buy/sell signals
    :return: DataFrame with backtest results
    """
    spread = price_series1 - price_series2
    signals = generate_signals(spread, z_score_threshold)
    
    # Calculate strategy returns
    strategy_returns = signals['signal'].shift(1) * (price_series1.pct_change() - price_series2.pct_change())
    signals['strategy_returns'] = strategy_returns
    
    return signals
