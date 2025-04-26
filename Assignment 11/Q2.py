import pandas as pd

# Given pandas series
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog'])

upper_case = s.str.upper()

lower_case = s.str.lower()

string_length = s.str.len()

print("Original Series:")
print(s)
print("\nUpper Case:")
print(upper_case)
print("\nLower Case:")
print(lower_case)
print("\nString Lengths:")
print(string_length)