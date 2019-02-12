# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def mom(df, price, mom, n):
    """
    Momentum is the measurement of the speed or velocity of price changes.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        mom (string): the column name for the rate of change values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with mom of the asset calculated.

    """

    df[price + "_n"] = df[price].shift(n)
    df[mom] = df[price] - df[price + "_n"]
    df = df.dropna().reset_index(drop=True)

    return df
