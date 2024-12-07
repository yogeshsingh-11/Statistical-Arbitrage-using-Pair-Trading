# Statistical Arbitrage using Pair Trading

## Overview
This project implements a pair trading strategy using historical price data. The strategy identifies pairs of assets that are cointegrated and mean-reverting, allowing for profitable trading opportunities based on spread movements. The project includes backtesting and analysis of the strategy's performance.

## Directory Structure
PairTradingArbitrage/ │ ├── src/ │ ├── pair_trading.py # Pair trading strategy logic │ ├── cointegration.py # Cointegration testing functions │ └── data_loader.py # Data loading and preprocessing functions │ ├── data/ │ └── asset_data.csv # Asset price data │ ├── notebooks/ │ └── strategy_backtest.ipynb # Jupyter notebook for backtesting and analysis │ ├── tests/ │ ├── test_pair_trading.py # Unit tests for pair trading │ └── test_cointegration.py # Unit tests for cointegration │ ├── requirements.txt # Required Python libraries ├── README.md # Project overview and setup instructions
