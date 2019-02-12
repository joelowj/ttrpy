# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
from ttrpy.trend.sma import sma
from ttrpy.util.trange import trange


def ultosc(
    df, high, low, close, ultosc, time_period_1, time_period_2, time_period_3
):
    """
    """

    df = trange(df, high, low, close, ultosc + "_true_range")
    df[ultosc + "previous_close"] = df[close].shift(1)
    df = df.dropna().reset_index(drop=True)
    df[ultosc + "_true_low"] = df[[low, ultosc + "previous_close"]].min(axis=1)
    df[ultosc + "_close-tl"] = df[close] - df[ultosc + "_true_low"]
    df = sma(df, ultosc + "_close-tl", ultosc + "_a1", time_period_1)
    df = sma(df, ultosc + "_true_range", ultosc + "_b1", time_period_1)
    df = sma(df, ultosc + "_close-tl", ultosc + "_a2", time_period_2)
    df = sma(df, ultosc + "_true_range", ultosc + "_b2", time_period_2)
    df = sma(df, ultosc + "_close-tl", ultosc + "_a3", time_period_3)
    df = sma(df, ultosc + "_true_range", ultosc + "_b3", time_period_3)
    df[ultosc + "_a1/b1"] = df[ultosc + "_a1"] / df[ultosc + "_b1"]
    df[ultosc + "_a2/b2"] = df[ultosc + "_a2"] / df[ultosc + "_b2"]
    df[ultosc + "_a3/b3"] = df[ultosc + "_a3"] / df[ultosc + "_b3"]
    df[ultosc] = (
        100
        * (
            (4 * df[ultosc + "_a1/b1"])
            + (2 * df[ultosc + "_a2/b2"])
            + df[ultosc + "_a3/b3"]
        )
        / 7.0
    )
    df.drop(
        [
            ultosc + "_true_range",
            ultosc + "previous_close",
            ultosc + "_true_low",
            ultosc + "_close-tl",
            ultosc + "_a1",
            ultosc + "_b1",
            ultosc + "_a2",
            ultosc + "_b2",
            ultosc + "_a3",
            ultosc + "_b3",
            ultosc + "_a1/b1",
            ultosc + "_a2/b2",
            ultosc + "_a3/b3",
        ],
        axis=1,
        inplace=True,
    )
    df = df.dropna().reset_index(drop=True)
    return df
