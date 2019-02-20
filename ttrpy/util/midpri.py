# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def midpri(df, high, low, midpri, n):
    """
    The Midprice returns the midpoint value from two different input fields. The
    default indicator calculates the highest high and lowest low within the look
    back period and averages the two values to return the Midprice.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the price of the asset.
        midpri (string): the column name for the calculated midprice values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with the midprice calculated.

    """

    midpri_hh = df[high].rolling(window=n).max()
    midpri_ll = df[low].rolling(window=n).min()
    df[midpri] = (midpri_hh + midpri_ll) / 2
    df = df.dropna().reset_index(drop=True)

    return df
