import pandas as pd
import os
data = {"name": ["Alice", "Bob", "Charlie"],"age": [25, 30, 35],"city": ["New York", "Los Angeles", "Chicago"]}
df = pd.DataFrame(data)

#adding a new row to df for version 2 of data
new_row_loc = {"name": "David", "age": 28, "city": "San Francisco"} # type: ignore
df.loc[len(df.index)] = new_row_loc

#adding new row to df for version 3 of data
new_row_loc = {"name": "Eve", "age": 22, "city": "Miami"} # type: ignore
df.loc[len(df.index)] = new_row_loc

#Ensureing the data directory exists at the root level 
data_dir = "data"
os.makedirs(data_dir,exist_ok=True)

#defining the file path
file_path = os.path.join(data_dir, "sample_data.csv")

#saving the datafram to the csv file including the column names
df.to_csv(file_path, index=False)

#displaying the dataframe 
print(f"CSV file saved at: {file_path}")