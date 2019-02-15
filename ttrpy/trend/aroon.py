# Author: joelowj
# License: Apache License, Version 2.0

import numpy as np
import pandas as pd


def aroon(df, high, low, aroon, n):
    """
    Aroon is an indicator system that determines whether a stock is trending or
    not and how strong the trend is. The Aroon indicators measure the number of
    periods since price recorded an x-day high or low. There are two separate
    indicators: Aroon-Up and Aroon-Down. Aroon indicators are quite different
    from typical momentum oscillators, which focus on price relative to time.
    Aroon is unique because it focuses on time relative to price. Aroon indicators
    can be use to spot emerging trends, identify consolidations, define correction
    periods and anticipate reversals.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        aroon (string): the column name for the results of aroon up and aroon down.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with aroon the asset calculated.

    """

    df[aroon + "_up"] = (
        df[high]
        .rolling(n)
        .apply(lambda x: float(np.argmax(x) + 1) / n * 100, raw=True)
    )
    df[aroon + "_dn"] = (
        df[low]
        .rolling(n)
        .apply(lambda x: float(np.argmin(x) + 1) / n * 100, raw=True)
    )
    df = df.dropna().reset_index(drop=True)

    return df
