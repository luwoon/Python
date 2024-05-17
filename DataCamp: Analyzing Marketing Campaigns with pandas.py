import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

daily_users = marketing.groupby(['date_served'])['user_id'].nunique()
print(daily_users.head())

# plot
daily_users.plot()
plt.title('Daily users')
plt.ylabel('Number of users')
plt.xticks(rotation=45)
plt.show()

# calculate conversion rate
total = marketing['user_id'].nunique()
subscribers = marketing[marketing['converted']==True]['user_id'].nunique()
conversion_rate = subscribers/total
print(round(conversion_rate*100, 2), "%")

# conversion rate for English speakers
english_speakers = marketing[marketing['language_displayed'] == 'English']
english_total = english_speakers['user_id'].nunique()
english_subscribers = english_speakers[english_speakers['converted']==True]['user_id'].nunique()
english_conversion_rate = english_subscribers/english_total
print('English speaker conversion rate:', round(conversion_rate*100,2), '%')

# compare conversion rate by language displayed
language_displayed_total = marketing.groupby(['language_displayed'])['user_id'].nunique()
language_displayed_subscribers = marketing[marketing['converted']==True].groupby(['language_displayed'])['user_id'].nunique()
language_conversion_rate = language_displayed_subscribers/language_displayed_total
print(language_conversion_rate)

# plot conversion rate by language displayed
language_conversion_rate.plot(kind='bar')
plt.title('Conversion rate by language\n', size = 16)
plt.xlabel('Language', size = 14)
plt.ylabel('Conversion rate (%)', size = 14)
plt.show()

# daily conversion rate
daily_total = marketing.groupby(['date_served'])['user_id'].nunique()
daily_subscribers = marketing[marketing['converted']==True].groupby(['date_served'])['user_id'].nunique()
daily_conversion_rate = daily_subscribers/daily_total
print(daily_conversion_rate)

# reset index to turn results into DataFrame
daily_conversion_rate = pd.DataFrame(daily_conversion_rates.reset_index())
daily_conversion_rate.columns = ['date_served', 
                              'conversion_rate']

# create line chart using daily_conversion_rate
daily_conversion_rate.plot('date_subscribed', 'conversion_rate')
plt.title('Daily conversion rate\n', size = 16)
plt.ylabel('Conversion rate (%)', size = 14)
plt.xlabel('Date', size = 14)
plt.ylim(0)
plt.show()

channel_age = marketing.groupby(['marketing_channel', 'age_group'])\
                                ['user_id'].count()

# unstack channel_age and transform it into a DataFrame
channel_age_df = pd.DataFrame(channel_age.unstack(level=1))

# plot marketing channel by age group
channel_age_df.plot(kind='bar')
plt.title('Marketing channels by age group')
plt.xlabel('Age Group')
plt.ylabel('Users')
# Add a legend to the plot
plt.legend(loc = 'upper right', 
           labels = channel_age_df.columns.values)
plt.show()

# calculate retention rate
retained = marketing[marketing['is_retained']==True]['user_id'].nunique()
retention_rate = retained/subscribers
print(round(retention_rate*100, 2), "%")

# find out which channel had the best retention rate and create plot
retention_total = marketing.groupby(['date_subscribed',
                                     'subscribing_channel'])['user_id'].nunique()
retention_subs = marketing[marketing['is_retained']==True].groupby(['date_subscribed', 'subscribing_channel'])['user_id'].nunique()
retention_rate = retention_subs/retention_total
retention_rate_df = pd.DataFrame(retention_rate.unstack(level=1))
retention_rate_df.plot()
plt.title('Retention Rate by Subscribing Channel')
plt.xlabel('Date Subscribed')
plt.ylabel('Retention Rate (%)')
plt.legend(loc = 'upper right', labels = retention_rate_df.columns.values)
plt.show()
