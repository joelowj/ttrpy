# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.util.tr import tr


class TestVolatilityIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_true_range(self):
        self.wdf = tr(self.wdf, "high", "low", "close", "tr")
        self.assertEqual(len(self.wdf["tr"]), 1100)
        self.assertAlmostEqual(self.wdf["tr"][0], 11.01, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1], 5.88, places=4)
        self.assertAlmostEqual(self.wdf["tr"][2], 11.88, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1096], 6.64, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1097], 3.02, places=4)
        self.assertAlmostEqual(self.wdf["tr"][1098], 5.0, places=4)

    def tearDown(self):
        self.ddf = None
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
