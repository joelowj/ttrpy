# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.ema import ema


def dema(df, price, dema, n):
    """
    Double Exponential Moving Average (DEMA) attempts to offer a smoothed average
    with less lag than a straight exponential moving average.

    The DEMA equation doubles the EMA, but then cancels out the lag by subtracting
    the square of the EMA.

    DEMA = 2 * EMA(p, n) - EMA(EMA(p, n), n)

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        dema (string): the column name for the n-day double exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day double exponential moving average of the asset calculated.

    """

    df = ema(df, price, dema + "_ema", n)
    df = ema(df[n - 1 :], dema + "_ema", dema + "_ema_2", n)
    df[dema] = 2 * df[dema + "_ema"] - df[dema + "_ema_2"]
    df = df.dropna().reset_index(drop=True)

    return df
