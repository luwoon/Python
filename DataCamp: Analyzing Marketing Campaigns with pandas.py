import pandas as pd
import numpy as np

marketing = pd.read_csv('marketing.csv', parse_dates=['date_served', 'date_subscribed', 'date_canceled'])

print(marketing.head())
print(marketing.describe())
print(marketing.info())

# change data type
print(marketing['is_retained'].dtype)
marketing['is_retained'] = marketing['is_retained'].astype('bool')
print(marketing['is_retained'].dtype)

# map values
channel_dict = {"House Ads": 1, "Instagram": 2, 
                "Facebook": 3, "Email": 4, "Push": 5}
marketing['channel_code'] = marketing['subscribing_channel'].map(channel_dict)

# add new column is_correct_lang
marketing['is_correct_lang'] = np.where(marketing['language_displayed'] == marketing['language_preferred'], 'Yes', 'No')

marketing['DoW'] = marketing['date_subscribed'].dt.dayofweek
