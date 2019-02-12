# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.volume.obv import obv


class TestVolumeIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_on_balance_volume(self):
        self.wdf = obv(self.wdf, "close", "volume", "obv")
        self.assertEqual(len(self.wdf["obv"]), 1101)
        self.assertAlmostEqual(self.wdf["obv"][0], 46857300.0, places=4)
        self.assertAlmostEqual(self.wdf["obv"][1], 87317200.0, places=4)
        self.assertAlmostEqual(self.wdf["obv"][2], 133939000.0, places=4)
        self.assertAlmostEqual(self.wdf["obv"][1097], 81836686.0000, places=4)
        self.assertAlmostEqual(self.wdf["obv"][1098], -30791892.0, places=4)
        self.assertAlmostEqual(self.wdf["obv"][1099], -232403105.0, places=4)

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
