from data_quality_tests import DataQuality as dq
import pandas as pd
import seaborn as sns
import json

df = sns.load_dataset("iris")
df2 = pd.util.testing.makeMixedDataFrame()

quality = dq(df)
change = dq(df2)

rows = quality.get_row_count()
print(rows)
print("")
quality.data_quality_check()
print("")
quality.generate_schema()
print("")
quality.print_schema()
print("")
quality.save_schema_to_file()
print("")
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



