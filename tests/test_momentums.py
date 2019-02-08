# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.momentum.rsi import rsi


class TestMomentumIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_relative_strength_index(self):
        self.wdf = rsi(self.wdf, "open", "rsi", 10)
        self.assertEqual(len(self.wdf["rsi"]), 1091)
        self.assertAlmostEqual(self.wdf["rsi"][0], 30.7729, places=4)
        self.assertAlmostEqual(self.wdf["rsi"][1], 30.4398, places=4)
        self.assertAlmostEqual(self.wdf["rsi"][2], 34.7525, places=4)
        self.assertAlmostEqual(self.wdf["rsi"][1088], 52.6662, places=4)
        self.assertAlmostEqual(self.wdf["rsi"][1089], 51.7396, places=4)
        self.assertAlmostEqual(self.wdf["rsi"][1090], 45.5756, places=4)

    def tearDown(self):
        self.ddf = None
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
