import pandas as pd

def load_asset_data(file_path):
    """
    Load asset data from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: DataFrame with asset price data
    """
    return pd.read_csv(file_path, index_col='Date', parse_dates=True)

def preprocess_data(df):
    """
    Preprocess the asset price data (e.g., resample, remove missing values).
    
    :param df: Raw asset data
    :return: Preprocessed DataFrame
    """
    df = df.dropna()
    return df

