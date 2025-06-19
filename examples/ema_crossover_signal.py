"""
Example: EMA Crossover Signal for an Indian stock (e.g., INFY.NS)

This script fetches data, calculates two EMAs (short and long), detects bullish crossovers,
and plots the results with signal markers.
"""

import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Local import (since not installed as pip package yet)
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantro.indicators.moving_average import ema
from quantro.signals.crossover import ema_crossover_signal

# Step 1: Download data
df = yf.download("INFY.NS", start="2024-06-01", end="2025-06-01", auto_adjust=True)
close = df["Close"]

# Step 2: Compute EMAs
short_span = 12
long_span = 26
short_ema = ema(close, span=short_span)
long_ema = ema(close, span=long_span)

# Step 3: Generate crossover signal (True where crossover happens)
signal = ema_crossover_signal(close, short_span=short_span, long_span=long_span)

# Step 4: Plot
plt.figure(figsize=(14, 7))
plt.plot(close, label="Close Price", color="black", alpha=0.6)
plt.plot(short_ema, label=f"EMA {short_span}", color="blue", linestyle="--")
plt.plot(long_ema, label=f"EMA {long_span}", color="red", linestyle="--")

# Mark crossover points
plt.scatter(signal[signal].index, close[signal], label="Buy Signal", color="green", marker="^", s=100)

plt.title("INFY.NS - EMA Crossover Strategy")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
