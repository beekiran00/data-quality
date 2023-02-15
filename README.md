# Project Descrption

## DATA QUALITY

A library which acts as a test cases for dataframes. Simply pass in your dataframe after initial import, or at each stage of your EDA to check for data quality with one line of code.

The test cases include(as of now)
1. check for null values
2. check for duplicates
3. check for dtype matching
4. check for outliers

The test cases work as a Pass/Fail type, where Passed indicates, good data quality and Failed indicates bad data quality

Example: 

TEST CASE FOR NULL VALUES: Passed means that the dataframe has no null values. Failed indicates otherwise.

## Requirements

* Python 3+
* Pandas
* Numpy


## Installation

```pip install data-quality-tests```

## Updates & Changes

1. the import function changed from:

```python
from data_quality import DataQuality
```

to the following:

```python
from data_quality_tests import DataQuality
```


## Get Started

How to use this library

```python
from data_quality_tests import DataQuality as dq

#declare any dataframe

df = sns.load_dataset("iris")

#pass the dataframe as below  

dq.data_quality_check(df)
```

