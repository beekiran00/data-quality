# DATA QUALITY

A library which acts as a test cases for dataframes. Simply pass in your dataframe after initial import, or at each stage of your EDA to check for data quality with one line of code.

The test cases include(as of now)
1. check for null values
2. check for duplicates
3. check for dtype matching
4. check for outliers

The test cases work as a Pass/Fail type, where Passed indicates, good data quality and Failed indicates bad data quality

Example: 

TEST CASE FOR NULL VALUES: Passed means that the dataframe has no null values. Failed indicates otherwise.

## Installation

`pip install data-quality-tests`

## Get Started

How to use this library

`from data_quality import DataQualityTests as dq`  

`#declare any dataframe`  

`df = sns.load_dataset("iris")`  

`#pass the dataframe as below`  

`dq.data_quality_check(df)`
