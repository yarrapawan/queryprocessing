import pandas as pd

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\sales_data.csv")

print("Original sales data:")
print(df)

pivot = pd.pivot_table(df, index=['Region', 'Manager', 'SalesMan'], values='Sale_amt', aggfunc='sum')

print("\nTotal sale amount region wise, manager wise, salesman wise:")
print(pivot)
