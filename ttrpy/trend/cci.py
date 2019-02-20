# Author: joelowj
# License: Apache License, Version 2.0

import numpy as np
import pandas as pd
from ttrpy.trend.sma import sma


def cci(df, high, low, close, cci, n, c=0.015):
    """
    The CCI is designed to detect beginning and ending market trends. The range
    of 100 to -100 is the normal trading range. CCI values outside of this range
    indicate overbought or oversold conditions. You can also look for price divergence
    in the CCI. If the price is making new highs, and the CCI is not, then a price
    correction is likely.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        cci (string): the column name for the cci values.
        n (int): the total number of periods.
        c (float): scaling factor to provide more readable numbers, usually 0.015.

    Returns:
        df (pd.DataFrame): Dataframe with commodity channel index calculated.

    """

    df[cci + "_tp"] = (df[high] + df[low] + df[close]) / 3.0
    df = sma(df, cci + "_tp", cci + "_atp", n)
    df[cci + "_mdev"] = (
        df[cci + "_tp"]
        .rolling(n)
        .apply(lambda x: np.fabs(x - x.mean()).mean(), raw=True)
    )
    df[cci] = (df[cci + "_tp"] - df[cci + "_atp"]) / (c * df[cci + "_mdev"])
    df.drop([cci + "_tp", cci + "_atp", cci + "_mdev"], axis=1, inplace=True)
    df = df.dropna().reset_index(drop=True)

    return df
