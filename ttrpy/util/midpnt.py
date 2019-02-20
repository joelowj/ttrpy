# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def midpnt(df, price, midpnt, n):
    """
    The Midpoint calculation is similar to the Midprice, except the highest and
    lowest values are returned from the same input field. The default indicator
    calculates the highest close and lowest close within the look back period
    and averages the two values.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the price of the asset.
        midpnt (string): the column name for the calculated midpoint values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with the midpoint calculated.

    """

    midpnt_max = df[price].rolling(window=n).max()
    midpnt_min = df[price].rolling(window=n).min()
    df[midpnt] = (midpnt_max + midpnt_min) / 2
    df = df.dropna().reset_index(drop=True)

    return df
