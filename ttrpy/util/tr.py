# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def tr(df, high, low, close, tr):
    """
    Welles Wilder described these calculations to determine the trading range
    for a stock or commodity. True Range is defined as the largest of the
    following:

    - The distance from today's high to today's low.
    - The distance from yesterday's close to today's high.
    - The distance from yesterday's close to today's low.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        tr (string): the column name for the tr values.

    Returns:
        df (pd.DataFrame): Dataframe with the true range calculated.

    """

    df["previous_close"] = df[close].shift(1)
    df["h-l"] = df[high] - df[low]
    df["h-pc"] = df[high] - df["previous_close"]
    df["pc-l"] = df["previous_close"] - df[low]
    df[tr] = df[["h-l", "h-pc", "pc-l"]].max(axis=1)
    df.drop(["h-l", "h-pc", "pc-l", "previous_close"], axis=1, inplace=True)

    return df
