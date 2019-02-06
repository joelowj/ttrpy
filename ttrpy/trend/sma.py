# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd

def sma(df, price, sma, n):
    """
    Simple Moving Average (SMA) is an arithmetic moving average calculated by
    adding recent closing prices then dividing that by the number of time periods
    in the calculation average.

    SMA = (P_1 + ... + P_n) / n

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        sma (string): the column name for the n-day moving average results.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with n-day moving average of the asset calculated.

    """

    df[sma] = df[price].rolling(window=n).mean()

    return df
