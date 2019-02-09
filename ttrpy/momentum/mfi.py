# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def mfi(df, high, low, close, volume, mfi, n):
    """
    The Money Flow Index (MFI) calculates the ratio of money flowing into and
    out of a security. To interpret the Money Flow Index, look for divergence
    with price to signal reversals. Money Flow Index values range from 0 to 100.
    Values above 80/below 20 indicate market tops/bottoms.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name of the volume of the asset.
        mfi (string): the column name for the mfi values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with mfi of the asset calculated.

    """

    df["typical_price"] = (df[high] + df[low] + df[close]) / 3
    df["money_flow"] = df["typical_price"] * df[volume]
    df["diff_typical_price"] = df["typical_price"].diff()
    df.loc[df["diff_typical_price"] > 0, "positive_money_flow"] = 1
    df.loc[df["diff_typical_price"] <= 0, "negative_money_flow"] = -1
    df["positive_money_flow"] *= df["money_flow"]
    df["negative_money_flow"] *= df["money_flow"]
    df = df.fillna(0)
    df["n_positive_money_flow"] = (
        df.loc[1:, "positive_money_flow"].rolling(window=n).sum()
    )
    df["n_negative_money_flow"] = (
        df.loc[1:, "negative_money_flow"].rolling(window=n).sum()
    )
    df[mfi + "_ratio"] = (
        df["n_positive_money_flow"] / -df["n_negative_money_flow"]
    )
    df[mfi] = 100 - (100 / (1 + df[mfi + "_ratio"]))
    df.drop(
        [
            "typical_price",
            "money_flow",
            "diff_typical_price",
            "positive_money_flow",
            "negative_money_flow",
            "n_positive_money_flow",
            "n_negative_money_flow",
            mfi + "_ratio",
        ],
        axis=1,
        inplace=True,
    )
    df = df.dropna().reset_index(drop=True)

    return df
