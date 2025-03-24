import pandas as pd
import numpy as np

#import dataset
df = pd.read_csv(r'C:\Users\Ahmed\Desktop\sonnen\measurements_coding_challenge.csv',delimiter=';')

#delete column direct_consumption
df = df.drop('direct_consumption',axis=1)

#Replace missing values with appropriate default values
df.fillna({'grid_purchase': 0, 'grid_feedin': 0}, inplace=True)

#Convert columns to their appropriate data types
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['grid_purchase'] = pd.to_numeric(df['grid_purchase'], errors='coerce').fillna(0).astype(int)
df['grid_feedin'] = pd.to_numeric(df['grid_feedin'], errors='coerce').fillna(0).astype(int)

#Remove duplicates and corrupt values from the dataset.
df.drop_duplicates(inplace=True)

#calculate the total grid_purchase and grid_feedin over all batteries for each hour of the day
df['hour'] = df['timestamp'].dt.hour
hourly_agg = df.groupby('hour')[['grid_purchase', 'grid_feedin']].sum().reset_index()

#Add a column to your dataframe that indicates the hour with the highest grid_feedin of the day
df['highest_grid_feedin_hour_of_day'] = df['hour'] == df.groupby('date')['grid_feedin'].transform('idxmax')

#save the output
df.to_csv(r'C:\Users\Ahmed\Desktop\sonnen\transformed_data.csv',index=False)