import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\job_history.csv")

print("Original job history data:")
print(df)

job_counts = df.groupby('EMPLOYEE_ID')['JOB_ID'].count()

result = job_counts[job_counts >= 2]

print("\nIDs of employees who have done two or more jobs in the past:")
print(result.index.tolist())
