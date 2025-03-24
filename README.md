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
