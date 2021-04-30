#! /usr/bin/Python

import pandas as pd
import numpy as np
import json
import os
import glob
import datetime

# Get the file path and read with glob library
file_src = r"C:\Users\jomen\Documents\self_project\dataproc-sparkjob\dataset"
files = glob.glob(file_src + "**\*.json", recursive=True)

# List of file name from the oldest file
files_name = ["2019-05-04.json","2019-05-05.json","2019-05-06.json","2019-05-07.json"]

# List for the updated value of flight_date for each file 
flights = ['2021-04-26',"2021-04-27","2021-04-28","2021-04-29"]

for i in range(len(files)):
    file_name = os.path.basename(files[i])
    for file_name in files_name:
        for flight in flights:
            df = pd.read_json("dataset/" + file_name, lines=True)
            df['flight_date'] = flight
            df_temp1 = df.groupby(['destination_airport']).agg({
            'id': ['count']
                }).reset_index()
            df_temp1.columns = ['destination_airport', 'count']
            df_temp1.sort_values('count', ascending=False)
            df = pd.merge(df, df_temp1, how='inner', on='destination_airport')
            df['most_visited'] = np.where(df['count'] >= 2823, 1, 0)
            df = df.drop(columns=['count'])

            df_temp2 = df.groupby(['source_airport']).agg({
                'id': ['count']
            }).reset_index()
            df_temp2.columns = ['source_airport', 'count']
            df_temp2.sort_values('count', ascending=False)
            df = pd.merge(df, df_temp2, how='inner', on='source_airport')
            df['most_come_from'] = np.where(df['count'] >= 199, 1, 0)
            df = df.drop(columns=['count','id'])
            
            # I used following object to handle the file name as the next 1 day of the flight_date
            flight_date = datetime.datetime.strptime(flight, "%Y-%m-%d")
            updated_date = flight_date.date()+datetime.timedelta(days=1)
            
            df.to_csv("new_dataset/" + str(updated_date) + ".csv", index=None, header=True)
            
            print("Done for " + str(updated_date) + ".csv")
            
            if str(updated_date) == "2021-04-30":
                break
        if str(updated_date) == "2021-04-30":
            break
    if str(updated_date) == "2021-04-30":
        break