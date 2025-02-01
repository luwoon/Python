import pandas as pd

df = pd.read_csv('BA_reviews.csv', header=None, names=['ID', 'reviews'], skiprows=1)


df[['verification', 'Review']] = df['reviews'].str.split('|', 1, expand=True)

df['Review'] = df['Review'].str.strip()
df['Review'] = df['Review'].apply(lambda x: x.strip('".'))

df['Verification_Status'] = df['verification'].apply(lambda x: 'Not Verified' if 'Not' in x else ('Verified' if 'Trip' in x else 'Unknown'))

df.drop(['reviews', 'verification'], axis=1, inplace=True)

df.to_csv('BA_reviews_cleaned.csv', index=False)