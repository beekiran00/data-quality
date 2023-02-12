import pandas as pd
import numpy as np


class DataQualityTests():
    """
    Initiate a data quality assessment class with (as of now) 4 test cases to check data quality
    """

    def __init__(self, df):
        self.df = df
    def data_quality_check(df):
        
        """
        
        Data Quality check 
        Input - dataset
        Output - data quality as test cases

        The out put will be in the form of the test cases below followed by Passed or Failed

        the test case checks are of conditional checks and logic that goes on in normal EDA.
        
        Checks include:
        
        1. Test for null values
        2. Test for duplicates
        3. Test for dtype matching
        4. Test for outliers                  
    
        """      
        
        # TEST FOR NULL VALUES
        # if null values exist -> condition = true then test failed, else false
        
        print("[=================================================================]")
        print("")
        
        #print("TEST FOR NULL VALUES:")
        print("")
        
        if df.isnull().values.any() == True:
            print("TEST CASE NULL VALUES: Failed")
        else:
            print('TEST CASE NULL VALUES: Passed')
            
        null_sum = df.isnull().sum().sum()
        
        #print("Total number of null values: ",null_sum)
        print("")

        
        
        # TEST FOR DUPLICATES
        
        if df.duplicated().any() == True:
            print("TEST CASE DUPLICATE VALUES: Failed")
        else:
            print("TEST CASE DUPLICATE VALUES: Passed")
        duplicate_sum = df.duplicated().sum()
        #print("Total number of duplicates: ", duplicate_sum)
        print("")
        
        # TEST For dtype matching
        
        num_list = df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).to_list()
        col_list = df.columns
        index_cols = list(zip(num_list, col_list))
        dtype_truth = []
        for i in index_cols:
            if i[0]==False:
                if df[i[1]].isna().any() == True:
                    pass
                elif any(df[i[1]].str.contains(r'\b.*[a-zA-Z]+.*\b')) == False:
                    my_truth = 'False'
                    dtype_truth.append(my_truth)
                else:
                    my_truth = 'True'
                    dtype_truth.append(my_truth)
            else:
                my_truth = 'True'
                dtype_truth.append(my_truth)
        fail = "False"
        if fail in dtype_truth:
            print('TEST CASE DTYPE MATCHING: Failed')
        else:
            print('TEST CASE DTYPE MATCHING: Passed')
        print("")


        # TEST FOR OUTLIERS
        

        
        cols_list = df.select_dtypes(include=['int32','int64','float']).columns
        outlier_truth_list =[]
        for i in cols_list:
            
            q1 = df[i].quantile(0.25)
            q3 = df[i].quantile(0.75)
            iqr = q3-q1 #Interquartile range
            fence_low  = q1-1.5*iqr
            fence_high = q3+1.5*iqr
            
            if len(df.loc[(df[i] > fence_low) & (df[i] < fence_high)]) > 0:
                truth = 'False'
                outlier_truth_list.append(truth)
            else:
                truth = 'True'
                outlier_truth_list.append(truth)
        if any('False' == 'False' for x in outlier_truth_list):
            print("TEST CASE OUTLIERS: Failed")
        else:
            print("TEST CASE OUTLIERS: Passed")
        print("")
        print("------------------------------------------------------------")
        print("[=================================================================]")
    
    