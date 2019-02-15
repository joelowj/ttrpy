# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.aroon import aroon


def aroonosc(df, high, low, aroonosc, n):
    """
    An Aroon Oscillator is a trend-following indicator that uses aspects of the
    Aroon Indicator ("Aroon Up" and "Aroon Down") to gauge the strength of a
    current trend and the likelihood that it will continue. The Aroon Oscillator
    is calculated by subtracting Aroon Up from Aroon Down.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        aroonosc (string): the column name for the results of aroonosc.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with aroonosc the asset calculated.

    """

    df = aroon(df, high, low, "aroon", n)
    df[aroonosc] = df["aroon_up"] - df["aroon_dn"]
    df.drop(["aroon_up", "aroon_dn"], axis=1, inplace=True)

    return df
