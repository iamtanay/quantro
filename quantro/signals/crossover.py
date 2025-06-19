"""
crossover.py

Signal functions for moving average crossovers and similar strategies.
"""

import pandas as pd
from quantro.indicators.moving_average import sma, ema


def ema_crossover_signal(series: pd.Series, short_span: int = 12, long_span: int = 26) -> pd.Series:
    """
    Generate signal when short-term EMA crosses above long-term EMA.

    Args:
        series (pd.Series): Price data (e.g., closing prices)
        short_span (int): Period for short-term EMA
        long_span (int): Period for long-term EMA

    Returns:
        pd.Series: Boolean Series where True means a bullish crossover
    """
    short_ema = ema(series, span=short_span)
    long_ema = ema(series, span=long_span)

    signal = (short_ema > long_ema) & (short_ema.shift(1) <= long_ema.shift(1))
    return signal
