# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def rsi(df, price, rsi, n):
    """
    The Relative Strength Index (RSI) is a momentum indicator that measures the
    magnitude of recent price changes to evaluate overbought or oversold
    conditions in the price of a stock or other asset.

    First calculations for average gain and average loss are simple n-period averages,
        1st average gain = sum of gains over the n periods / n
        1st average loss = sum of losses over the n periods / n

    Subsequent calculations are based on prior averages and the current gains / losses,
        average gain = (previous gain * (n - 1) + current gain) / n
        average loss = (previous loss * (n - 1) + current loss) / n

    RSI = 100 * (average gain / (average gain + average loss))

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset price.
        price (string): the column name of the price of the asset.
        rsi (string): the column name for the rsi values.
        n (int): the total number of periods.

    Returns:
        df (pd.DataFrame): Dataframe with rsi of the asset calculated.

    """

    df["diff"] = df[price].diff()
    df.loc[1:, "up"] = df[1:].loc[df["diff"] > 0, "diff"]
    df.loc[1:, "dn"] = -df[1:].loc[df["diff"] < 0, "diff"]
    prev_avg_gain = df[: n + 1].loc[df["diff"] > 0, "diff"].sum() / n
    prev_avg_loss = -df[: n + 1].loc[df["diff"] < 0, "diff"].sum() / n
    df.loc[n, "avg_gain"] = prev_avg_gain
    df.loc[n, "avg_loss"] = prev_avg_loss
    df = df.drop(df.index[:n]).reset_index(drop=True)
    df = df.fillna(0)
    avg_gains, avg_losses = [0.0], [0.0]
    for row in df.loc[1:, ["up", "dn"]].itertuples(index=False):
        avg_gains.append((prev_avg_gain * (n - 1) + row[0]) / n)
        avg_losses.append((prev_avg_loss * (n - 1) + row[1]) / n)
        prev_avg_gain, prev_avg_loss = avg_gains[-1], avg_losses[-1]
    df["avg_gain"] += avg_gains
    df["avg_loss"] += avg_losses
    df["rsi"] = 100 * df["avg_gain"] / (df["avg_gain"] + df["avg_loss"])
    del df["diff"], df["up"], df["dn"], df["avg_gain"], df["avg_loss"]

    return df
