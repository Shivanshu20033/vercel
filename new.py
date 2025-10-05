import pandas as pd

# Load data1.csv with CP-1252 encoding
data1 = pd.read_csv('data1.csv', encoding='cp1252')

# Load data2.csv with UTF-8 encoding
data2 = pd.read_csv('data2.csv', encoding='utf-8')

# Load data3.txt with UTF-16 encoding and tab separator
data3 = pd.read_csv('data3.txt', encoding='utf-16', sep='\t')

# Combine all dataframes
combined = pd.concat([data1, data2, data3])

# Filter rows where symbol is Š, Ž, or ™
filtered = combined[combined['symbol'].isin(['Š', 'Ž', '™'])]

# Sum all values in the filtered data
total_sum = filtered['value'].sum()

print("Total sum of values for symbols Š, Ž, and ™:", total_sum)
