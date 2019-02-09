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

    Fast Stochastic Oscillator:
        Fast %K = %K basic calculation
        Fast %D = n period moving average of Fast %K
    Slow Stochastic Oscillator:
        Slow %K =  Fast %K smoothed with n period moving average
        Slow %D = n-period moving average of Slow %K


    """

    ma_type = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df["highest_" + high] = df[high].rolling(window=fast_k_n).max()
    df["lowest_" + low] = df[low].rolling(window=fast_k_n).min()
    df["fast_%k"] = (
        (df[close] - df["lowest_" + low])
        / (df["highest_" + high] - df["lowest_" + low])
        * 100
    )
    df = ma_type[slow_k_ma_type](
        df[fast_k_n - 1 :], "fast_%k", "slow_%k", slow_k_n
    )
    df = ma_type[slow_d_ma_type](
        df[slow_k_n - 1 :], "slow_%k", "slow_%d", slow_d_n
    )
    df = df.dropna().reset_index(drop=True)
    del df["highest_" + high], df["lowest_" + low], df["fast_%k"]

    return df
