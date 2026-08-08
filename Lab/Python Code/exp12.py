import pandas as pd
import numpy as np

np.random.seed(24)

df = pd.DataFrame(np.random.rand(10, 4), columns=list('ABCD'))

print("Original DataFrame:")
print(df)

styled_df = df.style.set_properties(**{'background-color': 'black', 'color': 'yellow'})

print("\nDataFrame styled with black background and yellow font (styled object created).")
styled_df
