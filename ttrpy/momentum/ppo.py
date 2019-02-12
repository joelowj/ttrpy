# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema


def ppo(df, price, ppo, fast_period, slow_period, ma_type):
    """
    The Percentage Price Oscillator (PPO) is a momentum oscillator that measures
    the difference between two moving averages as a percentage of the larger
    moving average.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name of the price of the asset.
        ppo (string): the column name for the % price oscillator values.
        fast_period (int): the time period of the fast moving average.
        slow_period (int): the time period of the slow moving average.
        ma_type (int): Moving average type.

    Returns:
        df (pd.DataFrame): Dataframe with ppo of the asset calculated.

    """

    ma_types = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df = ma_types[ma_type](df, price, ppo + "_fast", fast_period)
    df = ma_types[ma_type](df, price, ppo + "_slow", slow_period)
    df[ppo] = (
        (df[ppo + "_fast"] - df[ppo + "_slow"]) / df[ppo + "_slow"]
    ) * 100
    df = df.dropna().reset_index(drop=True)

    return df
