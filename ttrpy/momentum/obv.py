# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def obv(df, price, volume, obv):
    """
    The On Balance Volume (OBV) is a cumulative total of the up and down volume.
    When the close is higher than the previous close, the volume is added to
    the running total, and when the close is lower than the previous close,
    the volume is subtracted from the running total.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        volume (string): the column name of the volume of the asset.
        obv (string): the column name for the on balance volume values.

    Returns:
        df (pd.DataFrame): Dataframe with obv of the asset calculated.

    """

    df["diff"] = df[price].diff()
    df = df.fillna(1)
    df.loc[df["diff"] > 0, obv + "_sign"] = 1
    df.loc[df["diff"] < 0, obv + "_sign"] = -1
    df.loc[df["diff"] == 0, obv + "_sign"] = 0
    df["volume_sign"] = df[volume] * df[obv + "_sign"]
    df[obv] = df["volume_sign"].cumsum()

    return df
