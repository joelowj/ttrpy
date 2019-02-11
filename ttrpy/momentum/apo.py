# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema


def apo(df, price, apo, fast_period, slow_period, ma_type):
    """
    The Absolute Price Oscillator (APO) shows the difference between two moving
    averages. It is basically a MACD, but the Price Oscillator can use any time
    periods. A buy signal is generate when the Price Oscillator rises above
    zero, and a sell signal when the it falls below zero.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        fast_period (int): the time period of the fast moving average.
        slow_period (int): the time period of the slow moving average.
        ma_type (int): Moving average type.

    Returns:
        df (pd.DataFrame): Dataframe with apo of the asset calculated.

    """

    ma_types = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df = ma_types[ma_type](df, price, apo + "_fast", fast_period)
    df = ma_types[ma_type](df, price, apo + "_slow", slow_period)
    df[apo] = df[apo + "_fast"] - df[apo + "_slow"]
    df = df.dropna().reset_index(drop=True)

    return df
