"""
Example: Plotting EMA and SMA for an Indian stock (e.g., RELIANCE.NS from Yahoo Finance)

This script demonstrates how to use the quantro library's moving average indicators
with externally fetched data. It does not depend on any internal data loading.
"""

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantro.indicators.moving_average import sma, ema

# Download RELIANCE data from Yahoo (free and works for NSE with .NS suffix)
df = yf.download("RELIANCE.NS", start="2024-06-01", end="2025-06-01", auto_adjust=True)
close = df["Close"]

# Compute indicators
sma_20 = sma(close, window=20)
ema_20 = ema(close, span=20)

# Plot the result
plt.figure(figsize=(12, 6))
plt.plot(close, label="Close Price", color="black", alpha=0.6)
plt.plot(sma_20, label="SMA (20)", color="blue", linestyle="--")
plt.plot(ema_20, label="EMA (20)", color="red")
plt.title("RELIANCE.NS - SMA vs EMA")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
