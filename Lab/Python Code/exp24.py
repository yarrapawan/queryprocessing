import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\fdata.csv", index_col='Date', parse_dates=True)

print("Financial data of Alphabet Inc.:")
print(df)

df.plot(figsize=(8, 5), marker='o')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc. Financial Data (Oct 3 - Oct 7, 2016)')
plt.tight_layout()
plt.show()
