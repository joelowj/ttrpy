# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def ad(df, high, low, close, volume, ad):
    """
    The Accumulation/Distribution Line is similar to the On Balance Volume (OBV),
    which sums the volume times +1/-1 based on whether the close is higher than
    the previous close. The Accumulation/Distribution indicator, however
    multiplies the volume by the close location value (CLV). The CLV is based on
    the movement of the issue within a single bar and can be +1, -1 or zero.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name for the volume of the asset.
        ad (string): the column name for the ad values.

    Returns:
        df (pd.DataFrame): Dataframe with ad of the asset calculated.

    """

    df[ad + "_money_flow_multiplier"] = (
        (df[close] - df[low]) - (df[high] - df[close])
    ) / (df[high] - df[low])
    df[ad + "_money_flow_volume"] = (
        df[ad + "_money_flow_multiplier"] * df[volume]
    )
    prev_ad = df.loc[0, ad + "_money_flow_volume"]
    df.loc[0, ad] = prev_ad
    ads = [0.0]
    for row in df.loc[1:, [ad + "_money_flow_volume"]].itertuples(index=False):
        ads.append(prev_ad + row[0])
        prev_ad = ads[-1]
    df = df.fillna(0)
    df[ad] += ads
    df.drop(
        [ad + "_money_flow_multiplier", ad + "_money_flow_volume"],
        axis=1,
        inplace=True,
    )

    return df
