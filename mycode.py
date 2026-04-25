import pandas as pd
import os
# sample data frame with column
data =  {'Name': ['John', 'Alice', 'Bob'],
         'Age': [25, 30, 22],
         'City': ['New York', 'Los Angeles', 'Chicago']}

df = pd.DataFrame(data)
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, 'mydata.csv')
# uploading data into csv file
df.to_csv(file_path, index=False)
print (df)