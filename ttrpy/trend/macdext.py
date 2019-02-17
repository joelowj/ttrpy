# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema


def macdext(
    df,
    price,
    macdext,
    fast_period,
    slow_period,
    signal_period,
    fast_ma_type=0,
    slow_ma_type=0,
    signal_ma_type=0,
):
    """
    The Moving Average Convergence Divergence (MACD) is the difference between
    two Exponential Moving Averages. The Signal line is an Exponential Moving
    Average of the MACD. The MACD signals trend changes and indicates the start
    of new trend direction. High values indicate overbought conditions, low values
    indicate oversold conditions. Divergence with the price indicates an end to
    the current trend, especially if the MACD is at extreme high or low values.
    When the MACD line crosses above the signal line a buy signal is generated.
    When the MACD crosses below the signal line a sell signal is generated. To
    confirm the signal, the MACD should be above zero for a buy, and below zero
    for a sell.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the series type of the asset.
        macd (string): the column name for the macd results.
        close (string): the column name for the closing price of the asset.
        fast_period (int): the time period of the fast exponential moving average.
        slow_period (int): the time period of the slow exponential moving average.
        signal_period (int): the time period of the macd signal.
        fast_ma_type (int): moving average type for the fast moving average.
        slow_ma_type (int): moving average type for the slow moving average.
        signal_ma_type (int): moving average type for the signal moving average.

    Returns:
        df (pd.DataFrame): Dataframe with macd of the asset calculated.

    """

    ma_types = {0: sma, 1: ema, 2: wma, 3: dema, 4: tema}

    df = ma_types[fast_ma_type](df, price, macdext + "_fast_ema", fast_period)
    df = ma_types[slow_ma_type](df, price, macdext + "_slow_ema", slow_period)
    df[macdext] = df[macdext + "_fast_ema"] - df[macdext + "_slow_ema"]
    df = ma_types[signal_ma_type](
        df[slow_period - 1 :], macdext, macdext + "_signal", signal_period
    )
    df[macdext + "_hist"] = df[macdext] - df[macdext + "_signal"]
    df.drop(
        [macdext + "_fast_ema", macdext + "_slow_ema"], axis=1, inplace=True
    )
    df = df.dropna().reset_index(drop=True)

    return df
