import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\sales_data.csv")

print("Original sales data:")
print(df)

pivot = pd.pivot_table(df, index='Item', values='Units', aggfunc='sum')

print("\nItem wise unit sold:")
print(pivot)
