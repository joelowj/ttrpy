# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd


def bop(df, open, high, low, close, bop):
    """
    Balance of Power (BOP) is used in technical analysis to evaluate the
    strength of buyers and sellers by assessing the ability to push price to
    extreme high and low levels. The Balance of Power oscillates around 0 (zero)
    center line in the range from -1 to +1. Positive BOP readings are considered
    as a bullish sign and negative BOP readings is a Bearish sign.

    Parameters:
        df (pd.DataFrame): DataFrame which contain the asset information.
        open (string): the column name for the opening price of the asset.
        high (string): the column name for the period highest price  of the asset.
        low (string): the column name for the period lowest price of the asset.
        close (string): the column name for the closing price of the asset.
        bop (string): the column name for the bop values.

    Returns:
        df (pd.DataFrame): Dataframe with balance of power calculated.

    """

    df[bop] = (df[close] - df[open]) / (df[high] - df[low])

    return df
