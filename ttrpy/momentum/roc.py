# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def roc(df, price, roc, n):
    """
    The Rate-of-Change (ROC) indicator, which is also referred to as simply
    Momentum, is a pure momentum oscillator that measures the percent change in
    price from one period to the next.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        roc (string): the column name for the rate of change values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with roc of the asset calculated.

    """

    price_shift_n = df[price].shift(n)
    df[roc] = ((df[price] - price_shift_n) / price_shift_n) * 100
    df = df.dropna().reset_index(drop=True)

    return df
