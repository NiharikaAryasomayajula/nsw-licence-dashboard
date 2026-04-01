#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import glob
import os

folder_path = "/Users/Niharikaarya/Desktop/Niha projects/tfnsw_driver_licence_transactions_2024/"

all_files = glob.glob(folder_path + "TfNSW*.csv")

df_list = []
for file in all_files:
    df = pd.read_csv(file, sep='|')
    filename = os.path.basename(file)
    parts = filename.split('_')
    month = parts[4]
    df['YEAR_MONTH'] = month
    df_list.append(df)

combined = pd.concat(df_list, ignore_index=True)
combined.columns = combined.columns.str.replace('"', '').str.strip()

print(combined.shape)
print(combined.columns.tolist())
print(combined['YEAR_MONTH'].unique())
combined.to_csv(folder_path + "2024_combined.csv", index=False)


# In[ ]:




