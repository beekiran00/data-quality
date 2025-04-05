import pandas as pd
import numpy as np


class DataQuality():
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
        4. Test for outliers - depricated
        5. Test for column header whitespaces               
    
        """      
        
        # TEST FOR NULL VALUES
        # if null values exist -> condition = true then test failed, else false
        
        
        #print("TEST FOR NULL VALUES:")
        print("Note:")
        print("Fail - Failed for test case due to existing condition.")
        print("Pass - Clear of condition.")
        
        if df.isnull().values.any() == True:
            print("Test Case Null Values: Fail")
        else:
            print('Test Case Null Values: Pass')
            
        null_sum = df.isnull().sum().sum()
        
        #print("Total number of null values: ",null_sum)
        print("")

        
        
        # TEST FOR DUPLICATES
        
        if df.duplicated().any() == True:
            print("Test Case Duplicated Values: Fail")
        else:
            print("Test Case Duplicated Values: Pass")
        #duplicate_sum = df.duplicated().sum()
        #print("Total number of duplicates: ", duplicate_sum)
        print("")
        


        # TEST For dtype matching
        
        # num_list is checking whether the columns are numeric or not-
        # a list of true and false where false is not number and true is number
        num_col_list_bool = df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).to_list()
        # col_list is a list of columns
        col_list = df.columns
        # index_cols is a list of tuples of the format - (bool,column_name) example - (False, 'booking_id')
        index_cols = list(zip(num_col_list_bool, col_list))
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
            print('Test Case Column Data Type Matches Values In Column: Fail')
        else:
            print('Test Case Column Data Type Matches Values In Column: Pass')
        print("")



        # # TEST FOR OUTLIERS
        # cols_list = df.select_dtypes(include=['int32','int64','float']).columns
        # outlier_truth_list =[]
        # for i in cols_list:
            
        #     q1 = df[i].quantile(0.25)
        #     q3 = df[i].quantile(0.75)
        #     iqr = q3-q1 #Interquartile range
        #     fence_low  = q1-1.5*iqr
        #     fence_high = q3+1.5*iqr
            
        #     if len(df.loc[(df[i] > fence_low) & (df[i] < fence_high)]) > 0:
        #         truth = 'False'
        #         outlier_truth_list.append(truth)
        #     else:
        #         truth = 'True'
        #         outlier_truth_list.append(truth)
        # if any('False' == 'False' for x in outlier_truth_list):
        #     print("TEST CASE OUTLIERS: Failed")
        # else:
        #     print("TEST CASE OUTLIERS: Passed")
        # print("")



        # TEST FOR COLUMN HEADER LEADING AND TRAILING SPACES
        col_list = [x for x in df.columns if x.endswith(' ') or x.startswith(' ')]
    
        if len(col_list) == 0:
            print("Test Case Column Header Whitespaces: Pass")
        else:
            print("Test Case Column Header Whitespaces: Fail")
        print("")



    # # DISPLAY LIST OF OUTLIER COLUMNS
    # def outlier_columns(df):
    #     """
    #     A function that checks for outliers and outputs the columns that have outliers
        
    #     Input - data frame
    #     Output - list of columns containing outliers
        
    #     """
        
    #     cols_list = df.select_dtypes(include=['int32','int64','float']).columns
    #     outlier_truth_list =[]
    #     for i in cols_list:
            
    #         q1 = df[i].quantile(0.25)
    #         q3 = df[i].quantile(0.75)
    #         iqr = q3-q1 #Interquartile range
    #         fence_low  = q1-1.5*iqr
    #         fence_high = q3+1.5*iqr
            
    #         if len(df.loc[(df[i] > fence_low) & (df[i] < fence_high)]) > 0:
    #             truth = 'False' #outliers
    #             outlier_truth_list.append(truth)
    #         else:
    #             truth = 'True' #not outliers
    #             outlier_truth_list.append(truth)
    #     truth_dict = dict(zip(cols_list, outlier_truth_list))

    #     filtered = [k for k, v in truth_dict.items() if v == 'False']
    #     print(filtered)

    
    # def dtype_columns(df):
    #     """
    #     A Function that checks for data type matching and outputs the list of columns that fail dtype matching
    #     Input - dataframe
    #     Output - list of columns that failed the test caset
    #     """

    #     # dtype matching columns
    
    #     num_list = df.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).to_list()
    #     col_list = df.columns
    #     index_cols = list(zip(num_list, col_list))

    #     dtype_truth = []
    #     dtype_column = []
    #     for i in index_cols:
    #         if i[0]==False:
    #             if df[i[1]].isna().any() == True:
    #                 pass
    #             elif any(df[i[1]].str.contains(r'\b.*[a-zA-Z]+.*\b')) == False:
    #                 my_truth = 'False'
    #                 dtype_truth.append(my_truth)
    #                 dtype_column.append(i[1])
    #             else:
    #                 my_truth = 'True'
    #                 dtype_truth.append(my_truth)
    #         else:
    #             my_truth = 'True'
    #             dtype_truth.append(my_truth)
                
    #     if len(dtype_column) != 0:
    #         print(dtype_column)
    #     else:
    #         print('THE COLUMNS AND DATA TYPES MATCH')

    # """def duplicated_columns(df):
  
    #     A function to display the columns of those which have duplicate values
    #     Input - Dataframe
    #     Output - List of columns which have duplicate values
     
    #     """

        


    


    
    