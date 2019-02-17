# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.volume.obv import obv
from ttrpy.volume.ad import ad
from ttrpy.volume.adosc import adosc


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

    def test_accumulation_distribution_line(self):
        self.wdf = ad(self.wdf, "high", "low", "close", "volume", "ad")
        self.assertEqual(len(self.wdf["ad"]), 1101)
        self.assertAlmostEqual(self.wdf["ad"][0], -33210715.2062, places=4)
        self.assertAlmostEqual(self.wdf["ad"][1], 6293728.4814, places=4)
        self.assertAlmostEqual(self.wdf["ad"][2], 27067387.6650, places=4)
        self.assertAlmostEqual(self.wdf["ad"][1097], -863010282.6314, places=4)
        self.assertAlmostEqual(self.wdf["ad"][1098], -803339512.8300, places=4)
        self.assertAlmostEqual(self.wdf["ad"][1099], -947882122.6143, places=4)

    def test_accumulation_distribution_oscillator(self):
        self.wdf = adosc(self.wdf, "high", "low", "close", "volume", "adosc", 5, 10)
        self.assertEqual(len(self.wdf["adosc"]), 1092)
        self.assertAlmostEqual(self.wdf["adosc"][1085], -35440220.0781, places=4)
        self.assertAlmostEqual(self.wdf["adosc"][1086], -25408687.2433, places=4)
        self.assertAlmostEqual(self.wdf["adosc"][1087], -19991295.8541, places=4)
        self.assertAlmostEqual(self.wdf["adosc"][1088], 6415945.8326, places=4)
        self.assertAlmostEqual(self.wdf["adosc"][1089], 29472076.3690, places=4)
        self.assertAlmostEqual(self.wdf["adosc"][1090], 18361565.7023, places=4)

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
