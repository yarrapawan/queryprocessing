import pandas as pd
import numpy as np

np.random.seed(24)

df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
df.iloc[3, 3] = np.nan

print("Original DataFrame:")
print(df)

def color_negative_red(val):
    color = 'red' if val < 0 else 'black'
    return 'color: %s' % color

styled_df = df.style.map(color_negative_red)

print("\nNegative numbers highlighted red, positive numbers highlighted black (styled object created).")
styled_df
