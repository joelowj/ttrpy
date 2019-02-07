# Author: joelowj
# License: Apache License, Version 2.0

import numpy as np
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
    df = df.drop(df.index[0]).reset_index(drop=True)
    df["up"] = df.loc[df["diff"] > 0, "diff"]
    df["dn"] = -df.loc[df["diff"] < 0, "diff"]
    df = df.fillna(0)

    df.loc[n - 1, "avg_gain"] = df[:n].loc[df["diff"] > 0, "diff"].sum() / n
    df.loc[n - 1, "avg_loss"] = -df[:n].loc[df["diff"] < 0, "diff"].sum() / n
    df = df.drop(df.index[: n - 1]).reset_index(drop=True)

    flag = True
    prev_avg_gain = df.loc[0, "avg_gain"]
    prev_avg_loss = df.loc[0, "avg_loss"]

    def calculate_avg(x):
        nonlocal flag, prev_avg_gain, prev_avg_loss
        if flag:
            flag = False
            return pd.Series({"avg_gain": avg_gain, "avg_loss": avg_loss})
        avg_gain = (prev_avg_gain * (n - 1) + x["up"]) / n
        avg_loss = (prev_avg_loss * (n - 1) + x["dn"]) / n
        prev_avg_gain = avg_gain
        prev_avg_loss = avg_loss
        return pd.Series({"avg_gain": avg_gain, "avg_loss": avg_loss})

    df.loc[1:, ["avg_gain", "avg_loss"]] = df.loc[1:, ["up", "dn"]].apply(
        lambda x: calculate_avg(x), axis=1
    )
    df["rsi"] = 100 * df["avg_gain"] / (df["avg_gain"] + df["avg_loss"])

    del df["diff"], df["up"], df["dn"], df["avg_gain"], df["avg_loss"]

    return df
