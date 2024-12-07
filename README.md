# Statistical Arbitrage using Pair Trading

## Overview
This project implements a pair trading strategy using historical price data. The strategy identifies pairs of assets that are cointegrated and mean-reverting, allowing for profitable trading opportunities based on spread movements. The project includes backtesting and analysis of the strategy's performance.

MonteCarloOptionPricing/
│
├── src/
│   ├── monte_carlo.py              # Contains the Monte Carlo simulation logic
│   ├── option_pricing.py           # Contains the option pricing formulas and Greeks
│   └── simulation.py               # Contains the logic for running the simulation and collecting results
│
├── notebooks/
│   └── monte_carlo_analysis.ipynb  # Jupyter notebook for Monte Carlo analysis and plotting results
│
├── tests/
│   ├── test_monte_carlo.py         # Unit tests for Monte Carlo simulation
│   └── test_option_pricing.py      # Unit tests for option pricing and Greeks
│
├── requirements.txt               # Required Python libraries (e.g., numpy, pandas, matplotlib)
├── README.md                      # Project overview and setup instructions
└── LICENSE                        # Project license

