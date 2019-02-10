# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def mom(df, price, mom, n):
    """
    """

    df[price + "_n"] = df[price].shift(n)
    df[mom] = df[price] - df[price + "_n"]
    df = df.dropna().reset_index(drop=True)

    return df
