'''
The purpose of this file is to move jsons into a CSV
for easy tokenization / NumPy stuff
'''


import os 
import json
import pandas as pd

all_data = []

directory_name = "./data_1/jsons"

for json_file in os.listdir(directory_name):
    if json_file.endswith('.json'):

        file_path = os.path.join(directory_name, json_file)
        with open(file_path, 'r') as file:
            data = json.load(file)

            df = pd.json_normalize(data)
            all_data.append(df)


final_df = pd.concat(all_data, ignore_index=True)

csv_file_path = "./combined_data.csv"
final_df.to_csv(csv_file_path, index=False)


