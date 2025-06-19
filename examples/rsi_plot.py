"""
Example: Plotting RSI for an Indian stock using quantro's RSI function.
"""

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Local import (since not yet pip-installed)
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantro.indicators.momentum import rsi

# Download Indian stock data
df = yf.download("TCS.NS", start="2024-06-01", end="2025-06-01", auto_adjust=True)
close = df["Close"]

# Compute RSI
rsi_14 = rsi(close, period=14)

# Plot price + RSI together
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

# Price chart
ax1.plot(close, label="TCS Close Price", color="black")
ax1.set_title("TCS.NS Price")
ax1.legend()
ax1.grid(True)

# RSI chart
ax2.plot(rsi_14, label="RSI (14)", color="purple")
ax2.axhline(70, color='red', linestyle='--', linewidth=1, label="Overbought (70)")
ax2.axhline(30, color='green', linestyle='--', linewidth=1, label="Oversold (30)")
ax2.set_title("Relative Strength Index (RSI)")
ax2.set_ylim(0, 100)
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()