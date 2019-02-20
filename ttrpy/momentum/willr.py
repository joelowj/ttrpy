# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def willr(df, high, low, close, willr, n):
    """
    Williams %R is a momentum indicator that reflects the level of the
    close relative to the highest high for the look-back period. %R corrects for the
    inversion by multiplying the raw value by -100. As a result, the Fast Stochastic
    Oscillator and Williams %R produce the exact same lines, only the scaling is different.
    Williams %R oscillates from 0 to -100. Readings from 0 to -20 are considered overbought.
    Readings from -80 to -100 are considered oversold. Unsurprisingly, signals derived
    from the Stochastic Oscillator are also applicable to Williams %R.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        willr (string): the column name for the willr values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with willr of the asset calculated.

    """

    hh = df[high].rolling(window=n).max()
    ll = df[low].rolling(window=n).min()
    df[willr] = -100 * (hh - df[close]) / (hh - ll)
    df = df.dropna().reset_index(drop=True)

    return df
