# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma


def trima(df, price, trima, n):
    """
    The Triangular Moving Average (TRIMA) is similar to other moving averages in
    that it shows the average (or mean) price over a specified number of data
    points (usually a number of price bars). However, the triangular moving average
    differs in that it is double smoothed—which also means averaged twice.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        trima (string): the column name for the n-day double exponential moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with triangular moving average of the asset calculated.

    """

    first_period_sma = None
    second_period_sma = None
    if n % 2 == 0:
        first_period_sma = int((n / 2) + 1)
        second_period_sma = int(n / 2)
    else:
        first_period_sma = int((n + 1) / 2)
        second_period_sma = int((n + 1) / 2)
    df = sma(df, price, trima + "_sma", first_period_sma)
    df = sma(
        df[first_period_sma - 1 :], trima + "_sma", trima, second_period_sma
    )
    df = df.dropna().reset_index(drop=True)
    df.drop([trima + "_sma"], axis=1, inplace=True)

    return df
