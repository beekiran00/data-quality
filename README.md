## DATA QUALITY

A library which acts as a test cases for dataframes, and other quality checks

The test cases include(as of now)
1. check for null values
2. check for duplicates
3. check for dtype matching

Quality checks include(as of now)
1. generate, save and compare dataframe schemas

The test cases work as a Pass/Fail type, where Passed indicates, good data quality and Failed indicates bad data quality. 

The dataframe schema is useful to check for possible schema drifts in your data pipelines.

Example: 

TEST CASE FOR NULL VALUES: Passed means that the dataframe has no null values. Failed indicates otherwise.

## Requirements

* Python 3+
* Pandas
* Numpy
* json
* datetime
* Dict
* typing


## Installation

```python
pip install data-quality-tests
```

## Updates & Changes

1. Usage of functions within the library has changed. previous you had to pass the dataframe to each function of the library. Now you simple have to pass it when initialising the module. Check get started section.


2. new function ```get_row_count()``` has been added in this update, which displays number of rows in a dataframe.  
*For use case, refer to the get started section*

3. ```data_quality_check()``` now checks for column header whitespaces for leading and trailing.

4. ```generate_schema()``` now generates a schema for any dataframe

5. ```print_schema()``` prints the schema of a dataframe

6. ```save_schema_to_file()``` saves the current dataframe schema to a file. The name of the dataframe is the variable name you give to the dataframe. Default value is "dataframe"

7. ```compare_with_schema(reference_schema)``` compares a current schema with already existing schema of your dataframe to check for schema drift.


## Get Started

How to use this library:

### Data quality check

The most basic usage of this library, here for simplifiction,  
let's just se the iris dataset from seaborn library as df. And to compare it to another dataframe for schema drift lets generate a dataframe.

You can use any dataset.

```python


from data_quality_tests import DataQuality as dq
import pandas as pd
import seaborn as sns
import json

# import two datasets
df = sns.load_dataset("iris") 
#generate this dataset
df2 = pd.util.testing.makeMixedDataFrame()

# initialise the Module
quality = dq(df)
change = dq(df2)

#get row count
rows = quality.get_row_count()
print(rows)
print("")
# check data quality
quality.data_quality_check()
print("")
# generate the schema of df passed in the quality variable
quality.generate_schema()
print("")
# print schema
quality.print_schema()
print("")
# save schema
change.save_schema_to_file()
print("")
# Compare schema drift
## after you run the save_schema_to_file function then use the saved schema.json file
## test.json is iris dataset. and change is new dataset created
with open('test.json', 'r') as f:
    reference_schema = json.load(f)
diff = change.compare_with_schema(reference_schema)
if diff.get("status") != "Schemas are identical":
    print("Schema drift detected!")
    print(diff)
else:
    print("Schema is same")

#dq.dtype_columns(df)

#df.head()


```
