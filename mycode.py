import pandas as pd
import os
# sample data frame with column
data =  {'Name': ['John', 'Alice', 'Bob'],
         'Age': [25, 30, 22],
         'City': ['New York', 'Los Angeles', 'Chicago']}
# Adding new row to the df
new_row = {'Name':'Ani', 'Age':32, 'City':'Kolkata'}
df = pd.DataFrame(data)
df.loc[len(df.index)] = new_row
new_row = {'Name':'Ani', 'Age':32, 'City':'Kolkata'}
# df = pd.DataFrame(data)
df.loc[len(df.index)] = new_row
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'mydata.csv')
# uploading data into csv file fine
df.to_csv(file_path, index=False)
print (df)