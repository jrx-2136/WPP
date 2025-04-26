import pandas as pd

# Sample DataFrame with 10 rows representing the next 10 days
data = {
    'day': range(1, 11),
    'John': [True, False, True, False, False, True, False, True, False, False],
    'Judy': [False, True, True, False, True, True, False, False, True, False]
}

df = pd.DataFrame(data)

df['party'] = df['John'] & df['Judy']

# Calculate days_til_party
days_til_party = []
for i in range(len(df)):
    if df.loc[i, 'party']:
        days_til_party.append(0)
    else:
        days_until = next((j - i for j in range(i + 1, len(df)) if df.loc[j, 'party']), len(df) - i)
        days_til_party.append(days_until)

df['days_til_party'] = days_til_party

df = df.drop(columns=['party'])

print(df)