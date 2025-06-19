"""
momentum.py

Implements momentum-based indicators like the Relative Strength Index (RSI).
"""

import pandas as pd


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    Compute the Relative Strength Index (RSI)

    Args:
        series (pd.Series): The price series (usually closing prices)
        period (int): The lookback period (default: 14)

    Returns:
        pd.Series: RSI values between 0 and 100
    """
    delta = series.diff()
    gain = delta.where(delta > 0, 0.0)
    loss = -delta.where(delta < 0, 0.0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
