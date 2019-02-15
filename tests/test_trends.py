# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.trend.sma import sma
from ttrpy.trend.wma import wma
from ttrpy.trend.ema import ema
from ttrpy.trend.dema import dema
from ttrpy.trend.tema import tema
from ttrpy.trend.trix import trix
from ttrpy.trend.bop import bop
from ttrpy.trend.aroon import aroon


class TestTrendIndicators(unittest.TestCase):
    def setUp(self):
        self.wdf = (
            pd.read_csv("examples/weekly_MSFT.csv")
            .sort_values(by="timestamp")
            .reset_index(drop=True)
        )

    def test_simple_moving_average(self):
        self.wdf = (
            sma(self.wdf, "open", "sma", 10).dropna().reset_index(drop=True)
        )
        self.assertEqual(len(self.wdf["sma"]), 1092)
        self.assertAlmostEqual(self.wdf["sma"][0], 124.8190, places=4)
        self.assertAlmostEqual(self.wdf["sma"][1], 119.9380, places=4)
        self.assertAlmostEqual(self.wdf["sma"][2], 115.5950, places=4)
        self.assertAlmostEqual(self.wdf["sma"][1089], 104.5530, places=4)
        self.assertAlmostEqual(self.wdf["sma"][1090], 104.3520, places=4)
        self.assertAlmostEqual(self.wdf["sma"][1091], 104.1600, places=4)

    def test_weighted_moving_average(self):
        self.wdf = (
            wma(self.wdf, "open", "wma", 10).dropna().reset_index(drop=True)
        )
        self.assertEqual(len(self.wdf["wma"]), 1092)
        self.assertAlmostEqual(self.wdf["wma"][0], 116.5182, places=4)
        self.assertAlmostEqual(self.wdf["wma"][1], 108.8129, places=4)
        self.assertAlmostEqual(self.wdf["wma"][2], 101.7678, places=4)
        self.assertAlmostEqual(self.wdf["wma"][1089], 103.5624, places=4)
        self.assertAlmostEqual(self.wdf["wma"][1090], 103.8727, places=4)
        self.assertAlmostEqual(self.wdf["wma"][1091], 103.6033, places=4)

    def test_exponential_moving_average(self):
        self.wdf = (
            ema(self.wdf, "open", "ema", 10).dropna().reset_index(drop=True)
        )
        self.assertEqual(len(self.wdf["ema"]), 1092)
        self.assertAlmostEqual(self.wdf["ema"][0], 124.8190, places=4)
        self.assertAlmostEqual(self.wdf["ema"][1], 117.1137, places=4)
        self.assertAlmostEqual(self.wdf["ema"][2], 110.5821, places=4)
        self.assertAlmostEqual(self.wdf["ema"][1089], 104.5003, places=4)
        self.assertAlmostEqual(self.wdf["ema"][1090], 104.8202, places=4)
        self.assertAlmostEqual(self.wdf["ema"][1091], 104.4656, places=4)

    def test_double_exponential_moving_average(self):
        self.wdf = dema(self.wdf, "open", "dema", 10)
        self.assertEqual(len(self.wdf["dema"]), 1083)
        self.assertAlmostEqual(self.wdf["dema"][0], 83.5329, places=4)
        self.assertAlmostEqual(self.wdf["dema"][1], 82.2401, places=4)
        self.assertAlmostEqual(self.wdf["dema"][2], 81.7171, places=4)
        self.assertAlmostEqual(self.wdf["dema"][1080], 102.9559, places=4)
        self.assertAlmostEqual(self.wdf["dema"][1081], 103.8184, places=4)
        self.assertAlmostEqual(self.wdf["dema"][1082], 103.3559, places=4)

    def test_triple_exponential_moving_average(self):
        self.wdf = (
            tema(self.wdf, "open", "tema", 10).dropna().reset_index(drop=True)
        )
        self.assertEqual(len(self.wdf["tema"]), 1074)
        self.assertAlmostEqual(self.wdf["tema"][0], 108.3352, places=4)
        self.assertAlmostEqual(self.wdf["tema"][1], 114.9284, places=4)
        self.assertAlmostEqual(self.wdf["tema"][2], 116.7212, places=4)
        self.assertAlmostEqual(self.wdf["tema"][1071], 102.5139, places=4)
        self.assertAlmostEqual(self.wdf["tema"][1072], 103.9007, places=4)
        self.assertAlmostEqual(self.wdf["tema"][1073], 103.3348, places=4)

    def test_triple_smooth_exponential_moving_average(self):
        self.wdf = trix(self.wdf, "close", "trix", 10)
        self.assertEqual(len(self.wdf["trix"]), 1073)
        self.assertAlmostEqual(self.wdf["trix"][0], -0.1181, places=4)
        self.assertAlmostEqual(self.wdf["trix"][1], 0.1188, places=4)
        self.assertAlmostEqual(self.wdf["trix"][2], 0.2755, places=4)
        self.assertAlmostEqual(self.wdf["trix"][1069], -0.2203, places=4)
        self.assertAlmostEqual(self.wdf["trix"][1070], -0.2046, places=4)
        self.assertAlmostEqual(self.wdf["trix"][1071], -0.2006, places=4)

    def test_balance_of_power(self):
        self.wdf = bop(self.wdf, "open", "high", "low", "close", "bop")
        self.assertEqual(len(self.wdf["bop"]), 1101)
        self.assertAlmostEqual(self.wdf["bop"][0], -0.5477, places=4)
        self.assertAlmostEqual(self.wdf["bop"][1], 0.9655, places=4)
        self.assertAlmostEqual(self.wdf["bop"][2], 0.7007, places=4)
        self.assertAlmostEqual(self.wdf["bop"][1097], 0.8750, places=4)
        self.assertAlmostEqual(self.wdf["bop"][1098], 0.1391, places=4)
        self.assertAlmostEqual(self.wdf["bop"][1099], -0.8074, places=4)

    def test_aroon(self):
        self.wdf = aroon(self.wdf, "high", "low", "aroon", 14)
        self.assertEqual(len(self.wdf["aroon_up"]), 1088)
        self.assertAlmostEqual(self.wdf["aroon_up"][1], 35.7143, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][1], 57.1429, places=4)
        self.assertAlmostEqual(self.wdf["aroon_up"][2], 28.5714, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][2], 50.0000, places=4)
        self.assertAlmostEqual(self.wdf["aroon_up"][3], 21.4286, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][3], 42.8571, places=4)
        self.assertAlmostEqual(self.wdf["aroon_up"][1084], 57.1429, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][1084], 78.5714, places=4)
        self.assertAlmostEqual(self.wdf["aroon_up"][1085], 50.0000, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][1085], 71.4286, places=4)
        self.assertAlmostEqual(self.wdf["aroon_up"][1086], 42.8571, places=4)
        self.assertAlmostEqual(self.wdf["aroon_dn"][1086], 64.2857, places=4)

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
