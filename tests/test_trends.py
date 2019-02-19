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
from ttrpy.trend.trima import trima
from ttrpy.trend.t3 import t3
from ttrpy.trend.macd import macd
from ttrpy.trend.macdext import macdext
from ttrpy.trend.bop import bop
from ttrpy.trend.aroon import aroon
from ttrpy.trend.aroonosc import aroonosc


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

    def test_triangular_moving_average(self):
        self.wdf = trima(self.wdf, "open", "trima", 10)
        self.assertEqual(len(self.wdf["trima"]), 1092)
        self.assertAlmostEqual(self.wdf["trima"][0], 134.1987, places=4)
        self.assertAlmostEqual(self.wdf["trima"][1], 127.8193, places=4)
        self.assertAlmostEqual(self.wdf["trima"][2], 117.9463, places=4)
        self.assertAlmostEqual(self.wdf["trima"][1088], 104.7717, places=4)
        self.assertAlmostEqual(self.wdf["trima"][1089], 103.7377, places=4)
        self.assertAlmostEqual(self.wdf["trima"][1090], 103.1233, places=4)

    def test_t3(self):
        self.wdf = t3(self.wdf, "open", "t3", 10, 0.7)
        self.assertEqual(len(self.wdf["t3"]), 1047)
        self.assertAlmostEqual(self.wdf["t3"][1040], 109.5147, places=4)
        self.assertAlmostEqual(self.wdf["t3"][1041], 108.6093, places=4)
        self.assertAlmostEqual(self.wdf["t3"][1042], 107.6079, places=4)
        self.assertAlmostEqual(self.wdf["t3"][1043], 106.5864, places=4)
        self.assertAlmostEqual(self.wdf["t3"][1044], 105.7145, places=4)
        self.assertAlmostEqual(self.wdf["t3"][1045], 105.0484, places=4)

    def test_moving_average_convergence_divergence(self):
        self.wdf = macd(self.wdf, "open", "macd", 12, 26, 9)
        self.assertEqual(len(self.wdf["macd"]), 1068)
        self.assertAlmostEqual(self.wdf["macd_hist"][1062], -1.6971, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1062], 0.2448, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1062], 1.9419, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1063], -1.6202, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1063], -0.0834, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1063], 1.5368, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1064], -1.4845, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1064], -0.3188, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1064], 1.1657, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1065], -1.0227, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1065], -0.1127, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1065], 0.9100, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1066], -0.7192, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1066], 0.0110, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1066], 0.7302, places=4)

    def test_moving_average_convergence_divergence_with_controllable_ma(self):
        self.wdf = macdext(self.wdf, "open", "macd", 12, 26, 9, 0, 0, 0)
        self.assertEqual(len(self.wdf["macd"]), 1068)
        self.assertAlmostEqual(self.wdf["macd_hist"][1062], -3.4112, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1062], -1.4322, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1062], 1.9790, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1063], -3.3148, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1063], -2.0378, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1063], 1.2770, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1064], -3.0742, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1064], -2.5215, places=4)
        self.assertAlmostEqual(self.wdf["macd_signal"][1064], 0.5527, places=4)
        self.assertAlmostEqual(self.wdf["macd_hist"][1065], -2.5231, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1065], -2.6517, places=4)
        self.assertAlmostEqual(
            self.wdf["macd_signal"][1065], -0.1287, places=4
        )
        self.assertAlmostEqual(self.wdf["macd_hist"][1066], -1.9038, places=4)
        self.assertAlmostEqual(self.wdf["macd"][1066], -2.6251, places=4)
        self.assertAlmostEqual(
            self.wdf["macd_signal"][1066], -0.7213, places=4
        )

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

    def test_aroon_oscillator(self):
        self.wdf = aroonosc(self.wdf, "high", "low", "aroonosc", 10)
        self.assertEqual(len(self.wdf["aroonosc"]), 1092)
        self.assertAlmostEqual(self.wdf["aroonosc"][0], -30.0, places=4)
        self.assertAlmostEqual(self.wdf["aroonosc"][1], -30.0, places=4)
        self.assertAlmostEqual(self.wdf["aroonosc"][2], -30.0, places=4)
        self.assertAlmostEqual(self.wdf["aroonosc"][1088], -30.0, places=4)
        self.assertAlmostEqual(self.wdf["aroonosc"][1089], -30.0, places=4)
        self.assertAlmostEqual(self.wdf["aroonosc"][1090], -30.0, places=4)

    def tearDown(self):
        self.wdf = None


if __name__ == "__main__":
    unittest.main()
