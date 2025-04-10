from data_quality_tests import DataQuality as dq
import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

dq.data_quality_check(df)

rows = dq.get_row_count(df)
print(rows)

#dq.dtype_columns(df)

#df.head()



