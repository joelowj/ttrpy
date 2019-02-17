# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.volume.ad import ad
from ttrpy.trend.ema import ema


def adosc(df, high, low, close, volume, adosc, fast_period, slow_period):
    """
    Marc Chaikin uses the Chaikin Oscillator to monitor the flow of money in and
    out of the market - comparing money flow to price action helps to identify
    tops and bottoms in short and intermediate cycles.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name for the volume of the asset.
        adosc (string): the column name for the adosc values.
        fast_period (int): the time period of the fast exponential moving average.
        slow_period (int): the time period of the slow exponential moving average.

    Returns:
        df (pd.DataFrame): Dataframe with adosc of the asset calculated.

    """

    df = ad(df, high, low, close, volume, adosc + "_ad")
    df = ema(df, adosc + "_ad", adosc + "_ad_fast", fast_period)
    df = ema(df, adosc + "_ad", adosc + "_ad_slow", slow_period)
    df[adosc] = df[adosc + "_ad_fast"] - df[adosc + "_ad_slow"]
    df = df.dropna().reset_index(drop=True)
    df.drop(
        [adosc + "_ad", adosc + "_ad_fast", adosc + "_ad_slow"],
        axis=1,
        inplace=True,
    )

    return df
