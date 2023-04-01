from data_quality_tests import DataQuality as dq
import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

dq.data_quality_check(df)

dq.outlier_columns(df)

dq.dtype_columns(df)

#df.head()



