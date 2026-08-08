import pandas as pd
import numpy as np

np.random.seed(24)

df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

df.iloc[1, 2] = np.nan
df.iloc[4, 0] = np.nan
df.iloc[6, 3] = np.nan
df.iloc[8, 1] = np.nan

print("Original DataFrame with NaN values:")
print(df)

styled_df = df.style.highlight_null(color='yellow')

print("\nNaN values highlighted in yellow (styled object created).")
styled_df
