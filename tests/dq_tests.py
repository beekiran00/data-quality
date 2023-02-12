import unittest
import pandas as pd
import numpy as np

from data_quality import DataQualityTests


import seaborn as sns

class DataQualityTestCases(unittest.TestCase):

    def setUp(self):
        self.dq = DataQualityTests

    def test_alpha(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")

        result = self.dq.data_quality_check(df)
        return result
    def test_no_df_input(self):


        try:
            self.dq.data_quality_check()
        except:
            print("data_quality_check takes 1 argument: None provided")

if __name__ == '__main__':
    unittest.main()