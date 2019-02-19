# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.ema import ema


def t3(df, price, t3, n, v_factor=0.7):
    """
    The T3 is a type of moving average, or smoothing function. It is based on the
    DEMA. The T3 takes the DEMA calculation and adds a vfactor which is between
    zero and 1. The resultant function is called the GD, or Generalized DEMA. A
    GD with vfactorof 1 is the same as the DEMA. A GD with a vfactor of zero is
    the same as an Exponential Moving Average. The T3 typically uses a vfactor
    of 0.7.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        t3 (string): the column name for the t3 moving average results.
        n (int): the total number of periods.
        v_factor (float): v factor is a volume factor between 0 and 1 which
                          determines how the moving averages responds.

    Returns:
        df (pd.DataFrame): Dataframe with t3 moving average of the asset calculated.

    """

    def gd(df, price, gd, n):
        df = ema(df, price, gd + "_ema", n)
        df = ema(df[n - 1 :], gd + "_ema", gd + "_ema_2", n)
        df[gd] = (1 + v_factor) * df[gd + "_ema"] - v_factor * df[
            gd + "_ema_2"
        ]
        df = df.dropna().reset_index(drop=True)
        df.drop([gd + "_ema", gd + "_ema_2"], axis=1, inplace=True)
        return df

    df = gd(df, price, t3 + "_gd_1", n)
    df = gd(df, t3 + "_gd_1", t3 + "_gd_2", n)
    df = gd(df, t3 + "_gd_2", t3, n)
    df.drop([t3 + "_gd_1", t3 + "_gd_2"], axis=1, inplace=True)

    return df
