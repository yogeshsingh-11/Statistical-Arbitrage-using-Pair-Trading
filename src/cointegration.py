from statsmodels.tsa.stattools import coint

def test_cointegration(series1, series2, significance_level=0.05):
    """
    Test the cointegration between two time series.
    
    :param series1: Time series of asset 1
    :param series2: Time series of asset 2
    :param significance_level: Significance level for cointegration test
    :return: Boolean indicating cointegration status
    """
    score, p_value, _ = coint(series1, series2)
    return p_value < significance_level

