# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.momentum.rsi import rsi
from ttrpy.momentum.stoch import stoch
from ttrpy.momentum.stochf import stochf
from ttrpy.momentum.mfi import mfi
from ttrpy.momentum.apo import apo
from ttrpy.momentum.ppo import ppo
from ttrpy.momentum.mom import mom
from ttrpy.momentum.roc import roc
from ttrpy.momentum.rocr import rocr


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

    def test_stochastic_oscillator_fast_0(self):
        self.wdf = stochf(self.wdf, "high", "low", "close", 5, 3, 0)

        self.assertAlmostEqual(self.wdf["fast_%k"][0], 81.0821, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][0], 90.7020, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1], 6.6675, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1], 60.1922, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][2], 4.3311, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][2], 30.6936, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1091], 98.6370, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1091], 63.5539, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1092], 94.7633, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1092], 81.4897, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1093], 52.1495, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1093], 81.8499, places=4)

    def test_stochastic_oscillator_fast_1(self):
        self.wdf = stochf(self.wdf, "high", "low", "close", 5, 3, 1)

        self.assertAlmostEqual(self.wdf["fast_%k"][0], 81.0821, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][0], 90.7020, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1], 6.6675, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1], 48.6847, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][2], 4.3311, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][2], 26.5079, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1091], 98.6370, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1091], 70.9933, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1092], 94.7633, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1092], 82.8783, places=4)

        self.assertAlmostEqual(self.wdf["fast_%k"][1093], 52.1495, places=4)
        self.assertAlmostEqual(self.wdf["fast_%d"][1093], 67.5139, places=4)

    def test_money_flow_index(self):
        self.wdf = mfi(self.wdf, "high", "low", "close", "volume", "mfi", 10)
        self.assertEqual(len(self.wdf["mfi"]), 1091)
        self.assertAlmostEqual(self.wdf["mfi"][0], 51.3815, places=4)
        self.assertAlmostEqual(self.wdf["mfi"][1], 52.2354, places=4)
        self.assertAlmostEqual(self.wdf["mfi"][2], 50.4667, places=4)
        self.assertAlmostEqual(self.wdf["mfi"][1087], 34.1296, places=4)
        self.assertAlmostEqual(self.wdf["mfi"][1088], 41.8414, places=4)
        self.assertAlmostEqual(self.wdf["mfi"][1089], 40.6965, places=4)

    def test_absolute_price_oscillator_0(self):
        self.wdf = apo(self.wdf, "close", "apo", 10, 26, 0)
        self.assertEqual(len(self.wdf["apo"]), 1076)
        self.assertAlmostEqual(self.wdf["apo"][0], -13.2494, places=4)
        self.assertAlmostEqual(self.wdf["apo"][1], -10.3612, places=4)
        self.assertAlmostEqual(self.wdf["apo"][2], -6.4765, places=4)
        self.assertAlmostEqual(self.wdf["apo"][1072], -3.2936, places=4)
        self.assertAlmostEqual(self.wdf["apo"][1073], -3.3860, places=4)
        self.assertAlmostEqual(self.wdf["apo"][1074], -3.2127, places=4)

    def test_percentage_price_oscillator_0(self):
        self.wdf = ppo(self.wdf, "close", "ppo", 10, 26, 0)
        self.assertEqual(len(self.wdf["ppo"]), 1076)
        self.assertAlmostEqual(self.wdf["ppo"][0], -12.6661, places=4)
        self.assertAlmostEqual(self.wdf["ppo"][1], -9.9556, places=4)
        self.assertAlmostEqual(self.wdf["ppo"][2], -6.2630, places=4)
        self.assertAlmostEqual(self.wdf["ppo"][1072], -3.0579, places=4)
        self.assertAlmostEqual(self.wdf["ppo"][1073], -3.1442, places=4)
        self.assertAlmostEqual(self.wdf["ppo"][1074], -2.9889, places=4)

    def test_momentum(self):
        self.wdf = mom(self.wdf, "close", "mom", 10)
        self.assertEqual(len(self.wdf["mom"]), 1091)
        self.assertAlmostEqual(self.wdf["mom"][0], -45.1900, places=4)
        self.assertAlmostEqual(self.wdf["mom"][1], -47.4400, places=4)
        self.assertAlmostEqual(self.wdf["mom"][2], -45.2500, places=4)
        self.assertAlmostEqual(self.wdf["mom"][1087], -1.8600, places=4)
        self.assertAlmostEqual(self.wdf["mom"][1088], -1.1200, places=4)
        self.assertAlmostEqual(self.wdf["mom"][1089], -0.2900, places=4)

    def test_rate_of_change(self):
        self.wdf = roc(self.wdf, "close", "roc", 10)
        self.assertEqual(len(self.wdf["roc"]), 1091)
        self.assertAlmostEqual(self.wdf["roc"][0], -35.5827, places=4)
        self.assertAlmostEqual(self.wdf["roc"][1], -35.0758, places=4)
        self.assertAlmostEqual(self.wdf["roc"][2], -32.7306, places=4)
        self.assertAlmostEqual(self.wdf["roc"][1087], -1.6975, places=4)
        self.assertAlmostEqual(self.wdf["roc"][1088], -1.0343, places=4)
        self.assertAlmostEqual(self.wdf["roc"][1089], -0.2814, places=4)

    def test_rate_of_change_ratio(self):
        self.wdf = rocr(self.wdf, "close", "rocr", 10)
        self.assertEqual(len(self.wdf["rocr"]), 1091)
        self.assertAlmostEqual(self.wdf["rocr"][0], 0.6442, places=4)
        self.assertAlmostEqual(self.wdf["rocr"][1], 0.6492, places=4)
        self.assertAlmostEqual(self.wdf["rocr"][2], 0.6727, places=4)
        self.assertAlmostEqual(self.wdf["rocr"][1087], 0.9830, places=4)
        self.assertAlmostEqual(self.wdf["rocr"][1088], 0.9897, places=4)
        self.assertAlmostEqual(self.wdf["rocr"][1089], 0.9972, places=4)

    def tearDown(self):
        self.ddf = None
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
