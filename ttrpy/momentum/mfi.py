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

    typical_price = (df[high] + df[low] + df[close]) / 3
    money_flow = typical_price * df[volume]
    typical_price_diff = typical_price.diff()
    df.loc[typical_price_diff > 0, "positive_money_flow"] = 1
    df.loc[typical_price_diff <= 0, "negative_money_flow"] = -1
    df["positive_money_flow"] *= money_flow
    df["negative_money_flow"] *= money_flow
    df = df.fillna(0)
    n_pos_money_flow = (
        df.loc[1:, "positive_money_flow"].rolling(window=n).sum()
    )
    n_neg_money_flow = (
        df.loc[1:, "negative_money_flow"].rolling(window=n).sum()
    )
    mfi_ratio = n_pos_money_flow / -n_neg_money_flow
    df[mfi] = 100 - (100 / (1 + mfi_ratio))
    df.drop(
        ["positive_money_flow", "negative_money_flow"], axis=1, inplace=True
    )
    df = df.dropna().reset_index(drop=True)

    return df
