# Sonnen-ETL-Battery-Time-Series-Project

##Project Objectives:
This project is consisting of CSV file containing battery time series data. The data has common data quality issues such as missing values, incorrect data types, and inconsistent formatting. The project develops an application that will transform and cleanse the data,and then write the cleaned data to an output file.

## Tech Used:
- Python
- Docker

### Data Transformation:

`1.`Import dataset:
```python
import pandas as pd
import numpy as np
df = pd.read_csv(r'C:\Users\Ahmed\Desktop\sonnen\measurements_coding_challenge.csv',delimiter=';')
df
```

`2.`delete column direct_consumption:
```python
df = df.drop('direct_consumption',axis=1)
```

`3.`Replace missing values with appropriate default values:
```python
df.fillna({'grid_purchase': 0, 'grid_feedin': 0}, inplace=True)
```

`4.`Convert columns to their appropriate data types:
```python
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['grid_purchase'] = pd.to_numeric(df['grid_purchase'], errors='coerce').fillna(0).astype(int)
df['grid_feedin'] = pd.to_numeric(df['grid_feedin'], errors='coerce').fillna(0).astype(int)
```

`5.`Remove duplicates and corrupt values from the dataset:
```python
df.drop_duplicates(inplace=True)
```

`6.`calculate the total grid_purchase and grid_feedin over all batteries for each hour of the day:
```python
df['hour'] = df['timestamp'].dt.hour
hourly_agg = df.groupby('hour')[['grid_purchase', 'grid_feedin']].sum().reset_index()
```

`7.`Add a column to your dataframe that indicates the hour with the highest grid_feedin of the day:
```python
df['highest_grid_feedin_hour_of_day'] = df['hour'] == df.groupby('date')['grid_feedin'].transform('idxmax')
```

`8.`Save Transformed dataset:
```python
df.to_csv(r'C:\Users\Ahmed\Desktop\sonnen\transformed_data.csv',index=False)
```

`9.`Get to the directory containing the Dockerfile and data_pipline.py file:
```python
cd C:\Users\Ahmed\Desktop\sonnen\data_pipeline.py
```

`10.`Build Docker Image:
```python
docker build -t data_pipeline:latest .
```

`11.`Run Container:
```python
docker run --rm -v "$(pwd):/app" data_pipeline:latest
```
