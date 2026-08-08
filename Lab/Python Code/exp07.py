import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\sales_data.csv")

print("Original sales data:")
print(df)

pivot = pd.pivot_table(df, index='Item', values='Sale_amt', aggfunc=['max', 'min'])

print("\nMaximum and minimum sale value of the items:")
print(pivot)
