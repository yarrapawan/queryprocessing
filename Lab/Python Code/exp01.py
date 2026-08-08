import pandas as pd
df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\employees.csv")
print("Original employees data:")
print(df)
distinct_dept = df['DEPARTMENT_ID'].unique()
print("\nDistinct department id from employees file:")
print(distinct_dept)