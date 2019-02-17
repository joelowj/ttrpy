# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def willr(df, high, low, close, willr, n):
    """
    """

    df[willr + "_highest_high"] = df[high].rolling(window=n).max()
    df[willr + "_lowest_low"] = df[low].rolling(window=n).min()
    df[willr] = (
        -100
        * (df[willr + "_highest_high"] - df[close])
        / (df[willr + "_highest_high"] - df[willr + "_lowest_low"])
    )
    df = df.dropna().reset_index(drop=True)
    df.drop(
        [willr + "_highest_high", willr + "_lowest_low"], axis=1, inplace=True
    )
    return df
