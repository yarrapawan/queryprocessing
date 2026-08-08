import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\jobs.csv")

print("Original jobs data:")
print(df)

result = df.sort_values('JOB_TITLE', ascending=False)

print("\nJobs details in descending order of job title:")
print(result)
