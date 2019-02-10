# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema


def stoch(
    df,
    high,
    low,
    close,
    fast_k_n,
    slow_k_n,
    slow_d_n,
    slow_k_ma_type=0,
    slow_d_ma_type=0,
):
    """
    The Stochastic Oscillator is another well-known momentum indicator used in
    technical analysis. The idea behind this indicator is that the closing
    prices should predominantly close in the same direction as the prevailing
    trend.

    In an upward trend the price should be closing near the highs of the trading
    range and in a downward trend the price should be closing near the lows of
    the trading range. When this occurs it signals continued momentum and
    strength in the direction of the prevailing trend.

    Fast Stochastic Oscillator:
        Fast %K = %K basic calculation
        Fast %D = n period moving average of Fast %K
    Slow Stochastic Oscillator:
        Slow %K =  Fast %K smoothed with n period moving average
        Slow %D = n-period moving average of Slow %K

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        fast_k_n (int): the time period of the fast k moving average.
        slow_k_n (int): the time period of the slow k moving average.
        slow_d_n (int): the time period of the slow d moving average.
        slow_k_ma_type (int): moving average type for the slow k moving average.
        slow_d_ma_type (int): Moving average type for the slow d moving average.

    Returns:
        df (pd.DataFrame): Dataframe with slow %k and slow %d of the asset calculated.

    """

    ma_types = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df["highest_" + high] = df[high].rolling(window=fast_k_n).max()
    df["lowest_" + low] = df[low].rolling(window=fast_k_n).min()
    df["fast_%k"] = (
        (df[close] - df["lowest_" + low])
        / (df["highest_" + high] - df["lowest_" + low])
        * 100
    )
    df = ma_types[slow_k_ma_type](
        df[fast_k_n - 1 :], "fast_%k", "slow_%k", slow_k_n
    )
    df = ma_types[slow_d_ma_type](
        df[slow_k_n - 1 :], "slow_%k", "slow_%d", slow_d_n
    )
    df = df.dropna().reset_index(drop=True)
    df.drop(
        ["highest_" + high, "lowest_" + low, "fast_%k"], axis=1, inplace=True
    )

    return df
