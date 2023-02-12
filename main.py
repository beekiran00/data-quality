from data_quality import DataQuality as dq
import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

dq.data_quality_check(df)

#df.head()



