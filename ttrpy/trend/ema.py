# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import numpy as np


def ema(df, price, ema, n):
    """
    Exponential Moving Average (EMA) is a Weighted Moving Average (WMA) that
    gives more weighting to recent price data than Simple Moving Average (SMA)
    does.

    The EMA formula is based on the previous day EMA value. Since we have to
    start our calculation somewhere, the initial value for our first EMA will
    actually be an SMA.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        ema (string): the column name for the n-day exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day exponential moving average of the asset calculated.

    """

    df = df.copy().reset_index(drop=True)
    k = 2.0 / (n + 1)
    prev_ema = list(df[:n][price].rolling(window=n).mean())[-1]
    df.loc[n - 1, ema] = prev_ema
    df.loc[n:, ema] = 0.0
    emas = [0.0 for i in range(n)]
    for row in df.loc[n:, [price]].itertuples(index=False):
        emas.append((k * row[0]) + ((1 - k) * prev_ema))
        prev_ema = emas[-1]
    df[ema] += emas

    return df
