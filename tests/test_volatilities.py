# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.volatility.atr import atr


class TestVolatilityIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_average_true_range(self):
        self.wdf = atr(self.wdf, "high", "low", "close", "atr", 14)
        self.assertEqual(len(self.wdf["atr"]), 1087)
        self.assertAlmostEqual(self.wdf["atr"][0], 11.8050, places=4)
        self.assertAlmostEqual(self.wdf["atr"][1], 11.4796, places=4)
        self.assertAlmostEqual(self.wdf["atr"][2], 10.9547, places=4)
        self.assertAlmostEqual(self.wdf["atr"][1083], 6.1786, places=4)
        self.assertAlmostEqual(self.wdf["atr"][1084], 5.9530, places=4)
        self.assertAlmostEqual(self.wdf["atr"][1085], 5.8849, places=4)

    def tearDown(self):
        self.ddf = None
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
