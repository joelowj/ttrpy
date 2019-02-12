# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.util.trange import trange
from ttrpy.util.midpnt import midpnt
from ttrpy.util.midpri import midpri


class TestUtilityIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_true_range(self):
        self.wdf = trange(self.wdf, "high", "low", "close", "tr")
        self.assertEqual(len(self.wdf["tr"]), 1100)
        self.assertAlmostEqual(self.wdf["tr"][0], 11.01, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1], 5.88, places=4)
        self.assertAlmostEqual(self.wdf["tr"][2], 11.88, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1096], 6.64, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1097], 3.02, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1098], 5.0, places=4)

    def test_midpoint(self):
        self.wdf = midpnt(self.wdf, "close", "midpoint", 10)
        self.assertEqual(len(self.wdf["midpoint"]), 1092)
        self.assertAlmostEqual(self.wdf["midpoint"][0], 120.25, places=4)
        self.assertAlmostEqual(self.wdf["midpoint"][1], 119.97, places=4)
        self.assertAlmostEqual(self.wdf["midpoint"][2], 119.97, places=4)
        self.assertAlmostEqual(self.wdf["midpoint"][1088], 104.56, places=4)
        self.assertAlmostEqual(self.wdf["midpoint"][1089], 104.56, places=4)
        self.assertAlmostEqual(self.wdf["midpoint"][1090], 104.56, places=4)

    def test_midprice(self):
        self.wdf = midpri(self.wdf, "high", "low", "midprice", 10)
        self.assertEqual(len(self.wdf["midprice"]), 1092)
        self.assertAlmostEqual(self.wdf["midprice"][0], 119.655, places=4)
        self.assertAlmostEqual(self.wdf["midprice"][1], 119.655, places=4)
        self.assertAlmostEqual(self.wdf["midprice"][2], 119.655, places=4)
        self.assertAlmostEqual(self.wdf["midprice"][1088], 103.69, places=4)
        self.assertAlmostEqual(self.wdf["midprice"][1089], 103.69, places=4)
        self.assertAlmostEqual(self.wdf["midprice"][1090], 103.69, places=4)

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
