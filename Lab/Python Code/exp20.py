import pandas as pd

df = pd.DataFrame({
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes']
})

print("Original DataFrame:")
print(df)

substring = "ar"
df['index_of_substring'] = df['name'].str.find(substring)

print(f"\nIndex position of substring '{substring}' in each row of the name column:")
print(df)
