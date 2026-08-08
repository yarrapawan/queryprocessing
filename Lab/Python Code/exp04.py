import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\Query Processing\DSA05_Lab\data_files\alphabet_stock_data.csv", parse_dates=['Date'], dayfirst=True)
df = df.sort_values('Date')

start_date = '2020-04-06'
end_date = '2020-04-24'
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
filtered_df = df.loc[mask]

print("Filtered stock data between", start_date, "and", end_date)
print(filtered_df)

plt.figure(figsize=(8, 5))
plt.plot(filtered_df['Date'], filtered_df['Close'], color='blue', marker='o')
plt.xlabel('Date')
plt.ylabel('Closing Stock Price')
plt.title('Alphabet Inc. Closing Stock Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
