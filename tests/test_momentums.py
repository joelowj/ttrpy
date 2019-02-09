# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.momentum.rsi import rsi
from ttrpy.momentum.stoch import stoch
from ttrpy.momentum.obv import obv


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

    def test_stochastic_oscillator_0(self):
        self.wdf = stoch(self.wdf, "high", "low", "close", 5, 3, 3, 0, 0)
        self.assertAlmostEqual(self.wdf["slow_%k"][0], 30.6936, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][0], 60.5293, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1], 4.9532, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1], 31.9463, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][2], 3.8074, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][2], 13.1514, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1089], 63.5539, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1089], 43.8390, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1090], 81.4897, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1090], 62.2441, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1091], 81.8499, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1091], 75.6312, places=4)

    def test_stochastic_oscillator_1(self):
        self.wdf = stoch(self.wdf, "high", "low", "close", 5, 3, 3, 1, 1)
        self.assertAlmostEqual(self.wdf["slow_%k"][0], 26.5079, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][0], 55.2982, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1], 15.1844, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1], 35.2413, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][2], 9.2074, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][2], 22.2243, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1089], 70.9933, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1089], 55.2069, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1090], 82.8783, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1090], 69.0426, places=4)
        self.assertAlmostEqual(self.wdf["slow_%k"][1091], 67.5139, places=4)
        self.assertAlmostEqual(self.wdf["slow_%d"][1091], 68.2783, places=4)

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
        self.ddf = None
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
