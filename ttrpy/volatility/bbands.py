# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema


def bbands(df, price, bbands, n_bdev_up, n_bdev_dn, ma_type, n):
    """
    Bollinger Bands are volatility bands placed above and below a moving average.
    Volatility is based on the standard deviation, which changes as volatility
    increases and decreases. The bands automatically widen when volatility
    increases and narrow when volatility decreases.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the desired price type of the asset.
        bbands (string): the column name for the bbands values.
        n_bdev_up (int): the standard deviation multiplier of the upper band.
        n_bdev_dn (int): the standard deviation multiplier of the lower band.
        ma_type (int): moving average type of the time series.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with average true range of the asset calculated.

    """

    ma_types = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df[price + "_n_days_std"] = df[price].rolling(window=n).std(ddof=0)
    df = ma_types[ma_type](df, price, bbands + "_middle_band", n)
    df[bbands + "_upper_band"] = df[bbands + "_middle_band"] + (
        df[price + "_n_days_std"] * n_bdev_up
    )
    df[bbands + "_lower_band"] = df[bbands + "_middle_band"] - (
        df[price + "_n_days_std"] * n_bdev_dn
    )
    del df[price + "_n_days_std"]
    df = df.dropna().reset_index(drop=True)

    return df
