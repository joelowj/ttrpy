# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.ema import ema
from ttrpy.volume.ad import ad


def adosc(df, high, low, close, volume, adosc, fast_period, slow_period):
    """
    The Chaikin oscillator measures the accumulation-distribution line of moving
    average convergence-divergence (MACD). Like other momentum indicators, this
    indicator is designed to anticipate directional changes in the Accumulation
    Distribution Line by measuring the momentum behind the movements. A momentum
    change is the first step to a trend change. Anticipating trend changes in the
    Accumulation Distribution Line can help chartists anticipate trend changes in
    the underlying security. The Chaikin Oscillator generates signals with crosses
    above/below the zero line or with bullish/bearish divergences.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        volume (string): the column name for the volume of the asset.
        adosc (string): the column name for the adosc values.
        fast_period (int): the time period of the fast EMA.
        slow_period (int): the time period of the slow EMA.

    Returns:
        df (pd.DataFrame): Dataframe with adosc of the asset calculated.

    """

    df = ad(df, high, low, close, volume, adosc + "_ad")
    df = ema(df, adosc + "_ad", adosc + "_fast_period", fast_period)
    df = ema(df, adosc + "_ad", adosc + "_slow_period", slow_period)
    df[adosc] = df[adosc + "_fast_period"] - df[adosc + "_slow_period"]
    df.drop(
        [adosc + "_ad", adosc + "_fast_period", adosc + "_slow_period"],
        axis=1,
        inplace=True,
    )
    df = df.dropna().reset_index(drop=True)
    return df
