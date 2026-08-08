import pandas as pd

df = pd.DataFrame({
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes']
})

print("Original DataFrame:")
print(df)

df['name_swapcase'] = df['name'].str.swapcase()

print("\nDataFrame with swapped case column:")
print(df)
