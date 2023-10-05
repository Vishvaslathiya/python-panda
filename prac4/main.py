# 1. Write a python script that loads the “Marks.csv” file and do the following:
# I.
# II.
# Add the “Total” column, which stores the total of all the subject marks.
# Add
# columns
# FOP_GRADES,
# DBMS_GRADES,
# CFO_GRADES,
# MATHS_GRADES, and PC_GRADES. These columns store the grades scored
# by the student based on subject marks. Grades calculated based on the
# given criteria:
# a. If the subject marks less than 40, then the grade is FF.
# b. If the subject marks between 40 to 50, then the grade is CC.
# c. If the subject marks between 50 to 60, then the grade is BC.
# d. If the subject marks between 60 to 70, then the grade is AB.
# e. If the subject marks greater than 70, then the grade is AA.
# III. Add the “Percentage” column, which stores the percentage.
# IV. Add the “Result Class” column, which stores the result of the student. The
# result will be considered based on the given criteria:
# a. If the student scores less than 40 marks in any subject or the
# percentage is less than 40, store the result “FAIL”.
# b. If the percentage is between 40 to 50, then store result “PASS”.
# c. If the percentage is between 50 to 60, then store result “SECOND”.
# d. If the percentage is between 60 to 70, then store result “FIRST”.
# e. If the percentage is greater than 70, then store result
# “DISTINCTION”.
# V.
# Print the name of the student who secured the 1 st Rank based on
# percentage.
# VI.
# VII.
# Print the name of the student who secured the minimum percentage.
# Store the updated csv file as result.csv.

import pandas as pd
import numpy as np

df = pd.read_csv('Marks.csv')
df['Total'] = df['FOP'] + df['DBMS'] + df['CFO'] + df['MATHS'] + df['PC']

df['FOP_GRADES'] = np.where(df['FOP'] < 40, 'FF', np.where(
    df['FOP'] < 50, 'CC', np.where(df['FOP'] < 60, 'BC', np.where(df['FOP'] < 70, 'AB', 'AA'))))
df['DBMS_GRADES'] = np.where(df['DBMS'] < 40, 'FF', np.where(
    df['DBMS'] < 50, 'CC', np.where(df['DBMS'] < 60, 'BC', np.where(df['DBMS'] < 70, 'AB', 'AA'))))
df['CFO_GRADES'] = np.where(df['CFO'] < 40, 'FF', np.where(
    df['CFO'] < 50, 'CC', np.where(df['CFO'] < 60, 'BC', np.where(df['CFO'] < 70, 'AB', 'AA'))))
df['MATHS_GRADES'] = np.where(df['MATHS'] < 40, 'FF', np.where(
    df['MATHS'] < 50, 'CC', np.where(df['MATHS'] < 60, 'BC', np.where(df['MATHS'] < 70, 'AB', 'AA'))))
df['PC_GRADES'] = np.where(df['PC'] < 40, 'FF', np.where(
    df['PC'] < 50, 'CC', np.where(df['PC'] < 60, 'BC', np.where(df['PC'] < 70, 'AB', 'AA'))))

df['Percentage'] = (df['Total'] / 500) * 100

df['Result Class'] = np.where(df['Percentage'] < 40, 'FAIL', np.where(df['Percentage'] < 50, 'PASS', np.where(
    df['Percentage'] < 60, 'SECOND', np.where(df['Percentage'] < 70, 'FIRST', 'DISTINCTION'))))

print(df.loc[df['Percentage'].idxmax()]['Name'])
print(df.loc[df['Percentage'].idxmin()]['Name'])

df.to_csv('result.csv', index=False)
