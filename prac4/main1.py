# 2. Write a python script that load the “Production.csv” file and do the following:
# I. Read the data from said csv file print the data.
# II. Print max, min value of 'Production' column.
# III. Print the “Mine Name/s” whose production is 0.
# IV. Print the second highest production.
# V. Print the third minimum labor hours.
# VI.
# Print the report for column Labor Hours, report contains count, mean,
# standard deviation, min, max, 25th percentile, 50th percentile, and 75th
# percentile.
# VII.
# Insert a column at the last position in the csv sheet and fill it with NaN
# values.
# VIII.
# Calculate and print the sum and average of the production and labor hours
# column.
# IX.
# Store the updated csv file as result.csv.

import pandas as pd
import numpy as np

df = pd.read_csv('Production.csv')

print(df['Production'].max())
print(df['Production'].min())

print(df.loc[df['Production'] == 0]['Mine Name/s'])

print(df['Production'].nlargest(2).iloc[-1])

print(df['Labor Hours'].nsmallest(3).iloc[-1])

print(df['Labor Hours'].describe())

df['New Column'] = np.nan

print(df['Production'].sum())
print(df['Production'].mean())
print(df['Labor Hours'].sum())
print(df['Labor Hours'].mean())

df.to_csv('result.csv', index=False)