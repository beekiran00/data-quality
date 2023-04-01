## DATA QUALITY

A library which acts as a test cases for dataframes. Simply pass in your dataframe after initial import, or at each stage of your EDA to check for data quality with one line of code.

The test cases include(as of now)
1. check for null values
2. check for duplicates
3. check for dtype matching
4. check for outliers
5. check for whitespaces in column headers

The test cases work as a Pass/Fail type, where Passed indicates, good data quality and Failed indicates bad data quality

Example: 

TEST CASE FOR NULL VALUES: Passed means that the dataframe has no null values. Failed indicates otherwise.

## Requirements

* Python 3+
* Pandas
* Numpy


## Installation

```python
pip install data-quality-tests
```

## Updates & Changes

1. the import function changed from:

```python
from data_quality import DataQuality
```

to the following:

```python
from data_quality_tests import DataQuality
```

2. new function ```outlier_columns``` has been added in this update, which displays all the columns that have outliers.  
*For use case, refer to the get started section*

3. ```data_quality_check``` now checks for column header whitespaces for leading and trailing.

4. new function ```dtype_columns``` has been added in this update, which displays all the columns that failed data type matching.
*For use case, refer the get started section*

## Get Started

How to use this library:

### Data quality check

The most basic usage of this library, here for simplifiction,  
let's just se the iris dataset from seaborn library.

You can use any dataset.

```python
from data_quality_tests import DataQuality as dq
import seaborn as sns

#declare any dataframe

df = sns.load_dataset("iris")

#pass the dataframe as below  

dq.data_quality_check(df)
```

### Outlier columns

Sometimes, the test case for outliers fails, this is because the dataset containes outliers.

use ```outier_columns(df)``` function to display all the columns that have outliers.  

*NOTE* *If the dataset does not have outlier columns, the output is an empty list.*


```python

# display columns that have outliers
dq.outlier_columns(df)

```

### Data type columns

When it is observed the test for dtype matching has failed, this is due to an error in the data type.
For example, sometimes numbers are in the form of strings.

use ```dtype_columns(df)``` function to display all the columns that failed data type matching.

```python
#display list of columns that failed dtype matching
dq.dtype_columns(df)
```