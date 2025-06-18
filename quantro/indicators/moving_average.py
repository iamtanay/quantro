"""
moving_average.py

Contains implementations of Simple Moving Average (SMA) and Exponential Moving Average (EMA).
"""

import pandas as pd


def sma(series: pd.Series, window: int) -> pd.Series:
    """
    Calculate Simple Moving Average (SMA)

    Args:
        series (pd.Series): The input price series (e.g., closing prices).
        window (int): The lookback period for the SMA.

    Returns:
        pd.Series: The SMA of the input series.
    """
    return series.rolling(window=window, min_periods=1).mean()


def ema(series: pd.Series, span: int) -> pd.Series:
    """
    Calculate Exponential Moving Average (EMA)

    Args:
        series (pd.Series): The input price series (e.g., closing prices).
        span (int): The span parameter for the EMA.

    Returns:
        pd.Series: The EMA of the input series.
    """
    return series.ewm(span=span, adjust=False).mean()
