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



