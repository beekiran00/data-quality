import unittest
import pandas as pd
import numpy as np

from data_quality_tests import DataQuality


import seaborn as sns

class DataQualityTestCases(unittest.TestCase):

    def setUp(self):
        self.dq = DataQuality

    def test_alpha(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")

        result = self.dq.data_quality_check(df)
        return result
    
    # def test_outlier_columns(self):
    #     """test whenn df is passed to outlier columns"""
    #     df = sns.load_dataset("iris")

    #     result = self.dq.outlier_columns(df)
    #     return result

    def test_no_df_input(self):


        try:
            self.dq.data_quality_check()
        except:
            print("data_quality_check takes 1 argument: None provided")
    
    # def test_no_df_input_outlier_colmns(self):

    #     try:
    #         self.dq.outlier_columns()
    #     except:
    #         print("outlier_column takes 1 argument: None provided")
    
    # def test_no_df_input_dtype_columns(self):
    #     try:
    #         self.dq.dtype_columns()
    #     except:
    #         print("dtype_columns takes 1 argument: None provided")


if __name__ == '__main__':
    unittest.main()