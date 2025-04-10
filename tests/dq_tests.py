import unittest
import pandas as pd
import numpy as np
import json

from data_quality_tests import DataQuality as dq


import seaborn as sns

class DataQualityTestCases(unittest.TestCase):

    def setUp(self):
        self.dq = dq

    def test_no_df_input(self):
        
        try:
            qual = dq()
        except:
            print("DataQuality takes 1 argument: None provided")
    
    

    def test_alpha(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        result = qual.data_quality_check()
        return result
    
    # def test_outlier_columns(self):
    #     """test whenn df is passed to outlier columns"""
    #     df = sns.load_dataset("iris")

    #     result = self.dq.outlier_columns(df)
    #     return result

    def test_get_row_count(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        result = qual.get_row_count()
        return result
    
    def test_generate_schema(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        result = qual.generate_schema()
        return result
    
    def test_print_schema(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        result = qual.print_schema()
        return result
    
    def test_save_schema(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        result = qual.save_schema_to_file()
        return result

    def test_fail_compare_schema(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        df2 = pd.util.testing.makeMixedDataFrame()
        change = dq(df2)
        try:
            result = change.compare_with_schema()
        except: 
            print("compare_with_schema takes a json file. None Provided")

    def test_compare_schema(self):
        """test when df is passed and everythiong works"""

        df = sns.load_dataset("iris")
        qual = dq(df)

        df2 = pd.util.testing.makeMixedDataFrame()
        change = dq(df2)

        with open('test.json', 'r') as f:
            reference_schema = json.load(f)
        try:
            result = change.compare_with_schema(reference_schema)
        except: 
            print("compare_with_schema takes a reference schema: None Provided")
    
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