# Author: joelowj
# License: Apache License, Version 2.0

import pandas as pd
import unittest
from ttrpy.trend.simple_moving_average import simple_moving_average as SMA
from ttrpy.trend.exponential_moving_average import exponential_moving_average as EMA

class TestTrendIndicators(unittest.TestCase):

    def setUp(self):
        self.df = pd.read_csv("examples/weekly_MSFT.csv") \
                    .sort_values(by="timestamp") \
                    .reset_index(drop=True)

    def test_simple_moving_average(self):
        self.df = SMA(self.df, 'open', 'sma', 10).dropna() \
                                                 .reset_index(drop=True)
        self.assertEqual(len(self.df['sma']), 1092)
        self.assertAlmostEqual(self.df['sma'][0], 124.8190, places=4)
        self.assertAlmostEqual(self.df['sma'][1], 119.9380, places=4)
        self.assertAlmostEqual(self.df['sma'][2], 115.5950, places=4)
        self.assertAlmostEqual(self.df['sma'][1089], 104.5530, places=4)
        self.assertAlmostEqual(self.df['sma'][1090], 104.3520, places=4)
        self.assertAlmostEqual(self.df['sma'][1091], 104.1600, places=4)

    def test_exponential_moving_average(self):
        self.df = EMA(self.df, 'open', 'ema', 10).dropna() \
                                                 .reset_index(drop=True)
        self.assertEqual(len(self.df['ema']), 1092)
        self.assertAlmostEqual(self.df['ema'][0], 124.8190, places=4)
        self.assertAlmostEqual(self.df['ema'][1], 117.1137, places=4)
        self.assertAlmostEqual(self.df['ema'][2], 110.5821, places=4)
        self.assertAlmostEqual(self.df['ema'][1089], 104.5003, places=4)
        self.assertAlmostEqual(self.df['ema'][1090], 104.8202, places=4)
        self.assertAlmostEqual(self.df['ema'][1091], 104.4656, places=4)

    def tearDown(self):
        self.df = None

if __name__ == '__main__':
    unittest.main()
