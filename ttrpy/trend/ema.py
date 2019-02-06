# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd

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

    series = pd.concat([df[:n][price].rolling(window=n).mean(),
                            df[n:][price]])
    df[ema] = series.ewm(span=n, adjust=False).mean()

    return df
