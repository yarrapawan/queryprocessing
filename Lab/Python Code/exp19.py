import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\world_alcohol.csv")

print("World alcohol consumption dataset (first 5 rows):")
print(df.head())

print("\nShape of the dataset (rows, columns):")
print(df.shape)

print("\nColumn names of the dataset:")
print(df.columns.tolist())
