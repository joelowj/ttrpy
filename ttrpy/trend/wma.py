# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def wma(df, price, wma, n):
    """
    The Weighted Moving Average calculates a weight for each value in the series.
    The more recent values are assigned greater weights. The Weighted Moving
    Average is similar to a Simple Moving average in that it is not cumulative,
    that is, it only includes values in the time period (unlike an Exponential
    Moving Average). The Weighted Moving Average is similar to an Exponential
    Moving Average in that more recent data has a greater contribution to the
    average.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        wma (string): the column name for the n-day weighted moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day weighted moving average of the asset calculated.

    """

    def wa(x):
        return sum([(i + 1) * p for i, p in enumerate(x)]) / (n * (n + 1) / 2)

    df[wma] = df[price].rolling(window=n).apply(lambda x: wa(x), raw=True)

    return df
