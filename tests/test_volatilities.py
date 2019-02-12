# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.volatility.atr import atr
from ttrpy.volatility.natr import natr
from ttrpy.volatility.bbands import bbands


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

    def test_normalized_average_true_range(self):
        self.wdf = natr(self.wdf, "high", "low", "close", "natr", 14)
        self.assertEqual(len(self.wdf["natr"]), 1087)
        self.assertAlmostEqual(self.wdf["natr"][0], 12.8148, places=4)
        self.assertAlmostEqual(self.wdf["natr"][1], 12.4616, places=4)
        self.assertAlmostEqual(self.wdf["natr"][2], 12.2235, places=4)
        self.assertAlmostEqual(self.wdf["natr"][1083], 5.7363, places=4)
        self.assertAlmostEqual(self.wdf["natr"][1084], 5.5547, places=4)
        self.assertAlmostEqual(self.wdf["natr"][1085], 5.7257, places=4)

    def test_bollinger_bands_0(self):
        self.wdf = bbands(self.wdf, "close", "bbands", 3, 3, 0, 5)
        self.assertEqual(len(self.wdf["bbands_middle_band"]), 1097)

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][0], 141.5640, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][0], 174.3052, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][0], 108.8228, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1], 147.6640, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1], 176.1670, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1], 119.1610, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][2], 151.6400, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][2], 173.8454, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][2], 129.4346, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1093], 102.2120, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1093], 111.6826, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1093], 92.7414, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1094], 104.0000, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1094], 112.7536, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1094], 95.2464, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1095], 104.4780, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1095], 111.8122, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1095], 97.1438, places=4
        )

    def test_bollinger_bands_1(self):
        self.wdf = bbands(self.wdf, "close", "bbands", 3, 3, 1, 5)
        self.assertEqual(len(self.wdf["bbands_middle_band"]), 1097)

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][0], 141.5640, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][0], 174.3052, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][0], 108.8228, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1], 146.8760, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1], 175.3790, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1], 118.3730, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][2], 149.6273, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][2], 171.8328, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][2], 127.4219, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1093], 104.2812, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1093], 113.7518, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1093], 94.8106, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1094], 105.2441, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1094], 113.9977, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1094], 96.4905, places=4
        )

        self.assertAlmostEqual(
            self.wdf["bbands_middle_band"][1095], 104.4227, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_upper_band"][1095], 111.7570, places=4
        )
        self.assertAlmostEqual(
            self.wdf["bbands_lower_band"][1095], 97.0885, places=4
        )

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
