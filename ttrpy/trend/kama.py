# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def kama(df, price, kama, n, fast_ema=2, slow_ema=30):
    """
    Kaufman's Adaptive Moving Average (KAMA) is a moving average designed to
    account for market noise or volatility. KAMA will closely follow prices when
    the price swings are relatively small and the noise is low. KAMA will adjust
    when the price swings widen and follow prices from a greater distance.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        price (string): the column name for the series type of the asset.
        kama (string): the column name for the kama results.
        n (int): the total number of periods.
        fast_ema (int): the time period of the fast exponential moving average.
        slow_ema (int): the time period of the slow exponential moving average.

    Returns:
        df (pd.DataFrame): Dataframe with kama of the asset calculated.

    """

    er = (
        df[price].diff(n).abs()
        / df[price].diff().abs().rolling(window=n).sum()
    )
    fast_sc = 2 / (fast_ema + 1)
    slow_sc = 2 / (slow_ema + 1)
    df[kama + "_sc"] = ((er * (fast_sc - slow_sc)) + slow_sc) ** 2
    prev_kama = list(df[:n][price].rolling(window=n).mean())[-1]
    df.loc[n - 1, kama] = prev_kama
    df.loc[n:, kama] = 0.0
    kamas = [0.0 for i in range(n)]
    for row in df.loc[n:, [price, kama + "_sc"]].itertuples(index=False):
        kamas.append(prev_kama + row[1] * (row[0] - prev_kama))
        prev_kama = kamas[-1]
    df[kama] += kamas
    df = df.dropna().reset_index(drop=True)
    df.drop([kama + "_sc"], axis=1, inplace=True)

    return df
