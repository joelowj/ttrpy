# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest

from ttrpy.trend.sma import sma
from ttrpy.trend.ema import ema
from ttrpy.trend.wma import wma

class TestTrendIndicators(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv("examples/weekly_MSFT.csv") \
                    .sort_values(by="timestamp") \
                    .reset_index(drop=True)

    def test_simple_moving_average(self):
        self.df = sma(self.df, 'open', 'sma', 10).dropna() \
                                                 .reset_index(drop=True)
        self.assertEqual(len(self.df['sma']), 1092)
        self.assertAlmostEqual(self.df['sma'][0], 124.8190, places=4)
        self.assertAlmostEqual(self.df['sma'][1], 119.9380, places=4)
        self.assertAlmostEqual(self.df['sma'][2], 115.5950, places=4)
        self.assertAlmostEqual(self.df['sma'][1089], 104.5530, places=4)
        self.assertAlmostEqual(self.df['sma'][1090], 104.3520, places=4)
        self.assertAlmostEqual(self.df['sma'][1091], 104.1600, places=4)

    def test_exponential_moving_average(self):
        self.df = ema(self.df, 'open', 'ema', 10).dropna() \
                                                 .reset_index(drop=True)
        self.assertEqual(len(self.df['ema']), 1092)
        self.assertAlmostEqual(self.df['ema'][0], 124.8190, places=4)
        self.assertAlmostEqual(self.df['ema'][1], 117.1137, places=4)
        self.assertAlmostEqual(self.df['ema'][2], 110.5821, places=4)
        self.assertAlmostEqual(self.df['ema'][1089], 104.5003, places=4)
        self.assertAlmostEqual(self.df['ema'][1090], 104.8202, places=4)
        self.assertAlmostEqual(self.df['ema'][1091], 104.4656, places=4)

    def test_weighted_moving_average(self):
        self.df = wma(self.df, 'open', 'wma', 10).dropna() \
                                                 .reset_index(drop=True)
        self.assertEqual(len(self.df['wma']), 1092)
        self.assertAlmostEqual(self.df['wma'][0], 116.5182, places=4)
        self.assertAlmostEqual(self.df['wma'][1], 108.8129, places=4)
        self.assertAlmostEqual(self.df['wma'][2], 101.7678, places=4)
        self.assertAlmostEqual(self.df['wma'][1089], 103.5624, places=4)
        self.assertAlmostEqual(self.df['wma'][1090], 103.8727, places=4)
        self.assertAlmostEqual(self.df['wma'][1091], 103.6033, places=4)


    def tearDown(self):
        self.df = None

if __name__ == '__main__':
    unittest.main()
