# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.ema import ema


def macd(df, price, macd, fast_period, slow_period, signal_period):
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

    Returns:
        df (pd.DataFrame): Dataframe with macd of the asset calculated.

    """

    df = ema(df, price, macd + "_fast_ema", fast_period)
    df = ema(df, price, macd + "_slow_ema", slow_period)
    df[macd] = df[macd + "_fast_ema"] - df[macd + "_slow_ema"]
    df = ema(df[slow_period - 1 :], macd, macd + "_signal", signal_period)
    df[macd + "_hist"] = df[macd] - df[macd + "_signal"]
    df.drop([macd + "_fast_ema", macd + "_slow_ema"], axis=1, inplace=True)
    df = df.dropna().reset_index(drop=True)

    return df
