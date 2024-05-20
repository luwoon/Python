import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

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

def conversion_rate(dataframe, column_names):
    column_conv = dataframe[dataframe['converted']==True].groupby(column_names)['user_id'].nunique()
    column_total = dataframe.groupby(column_names)['user_id'].nunique()  
    conversion_rate = column_conv/column_total
    conversion_rate = conversion_rate.fillna(0)
    return conversion_rate

def plotting_conv(dataframe):
    for column in dataframe:
        plt.plot(dataframe.index, dataframe[column])
        plt.title('Daily ' + str(column) + ' conversion rate\n', 
                  size = 16)
        plt.ylabel('Conversion rate', size = 14)
        plt.xlabel('Date', size = 14)
        plt.show()
        plt.clf()

# calculate conversion rate by age_group and visualise
age_group_conv = conversion_rate(marketing, ['date_served', 'age_group'])
print(age_group_conv)
age_group_df = pd.DataFrame(age_group_conv.unstack(level=1))
plotting_conv(age_group_df)

# daily conversion rate 
daily_conv_channel = conversion_rate(marketing, ['date_served', 'marketing_channel'])
daily_conv_channel = pd.DataFrame(daily_conv_channel.unstack(level = 1))
plotting_conv(daily_conv_channel)

# check whether users are more likely to convert on weekends compared with weekday
marketing['DoW_served'] = marketing['date_served'].dt.dayofweek
DoW_conversion = conversion_rate(marketing, ['DoW_served', 'marketing_channel'])
DoW_df = pd.DataFrame(DoW_conversion.unstack(level=1))
DoW_df.plot()
plt.title('Conversion rate by day of week\n')
plt.ylim(0)
plt.show()

# conversion by language over time
house_ads = marketing[marketing['marketing_channel'] == 'House Ads']
conv_lang_channel = conversion_rate(house_ads, ['date_served', 'language_displayed'])
conv_lang_df = pd.DataFrame(conv_lang_channel.unstack(level=1))
plotting_conv(conv_lang_df)

house_ads['is_correct_lang'] = np.where(house_ads['language_displayed'] == house_ads['language_preferred'], 'Yes', 'No')
language_check = house_ads.groupby(['date_served', 'is_correct_lang'])['user_id'].count()
language_check_df = pd.DataFrame(language_check.unstack(level=1)).fillna(0)
print(language_check_df)
language_check_df['pct'] = language_check_df['Yes']/language_check_df.sum(axis=1)
plt.plot(language_check_df.index.values, language_check_df['pct'])
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

# index non-English language conversion rates against English conversion rates in the time period before the language b
house_ads_bug = house_ads[house_ads['date_served'] < '2018-01-11']
lang_conv = conversion_rate(house_ads_bug, 'language_displayed')
spanish_index = lang_conv['Spanish']/lang_conv['English']
arabic_index = lang_conv['Arabic']/lang_conv['English']
german_index = lang_conv['German']/lang_conv['English']
print("Spanish index:", spanish_index)
print("Arabic index:", arabic_index)
print("German index:", german_index)

converted = house_ads.groupby(['date_served', 'language_preferred']).agg({'user_id':'nunique', 'converted':'sum'})
converted_df = pd.DataFrame(converted.unstack(level=1))

# create English conversion rate column for affected period
converted['english_conv_rate'] = converted.loc['2018-01-11': '2018-01-31'][('converted', 'English')]

# create expected conversion rates for each language
converted['expected_spanish_rate'] = converted['english_conv_rate']*spanish_index
converted['expected_arabic_rate'] = converted['english_conv_rate']*arabic_index
converted['expected_german_rate'] = converted['english_conv_rate']*german_index

# multiply number of users by the expected conversion rate
converted['expected_spanish_conv'] = converted['expected_spanish_rate']*converted[('user_id', 'Spanish')]/100
converted['expected_arabic_conv'] = converted['expected_arabic_rate']*converted[('user_id', 'Arabic')]/100
converted['expected_german_conv'] = converted['expected_german_rate']*converted[('user_id', 'German')]/100

converted = converted.loc['2018-01-11':'2018-01-31']
expected_subs = converted['expected_spanish_conv'].sum() + converted['expected_arabic_conv'].sum() + converted['expected_german_conv'].sum()
# calculate actual number of subscribers
actual_subs = converted[('converted','Spanish')].sum() + converted[('converted','Arabic')].sum() + converted[('converted','German')].sum()
lost_subs = expected_subs - actual_subs
print(lost_subs)

# A/B testing
# allocation
email = marketing[marketing['marketing_channel'] == 'Email']
alloc = email.groupby('variant')['user_id'].nunique()
alloc.plot(kind='bar')
plt.title('Personalization test allocation')
plt.ylabel('# participants')
plt.show()

subscribers = email.groupby(['user_id', variant'])['converted'].max()
subscribers_df = pd.DataFrame(subscribers.unstack(level=1)) 
control = subscribers_df['control'].dropna()
personalization = subscribers_df['personalization'].dropna()
print('Control conversion rate:', np.mean(control))
print('Personalization conversion rate:', np.mean(personalization))

def lift(a,b):
    a_mean = np.mean(a)
    b_mean = np.mean(b)
    lift = (b_mean-a_mean)/a_mean
    return str(round(lift*100, 2)) + '%'
  
# print lift() with control and personalization as inputs
print(lift(control, personalization))

def ab_segmentation(segment):g
  for subsegment in np.unique(marketing[segment].values):
      print(subsegment)
      email = marketing[(marketing['marketing_channel'] == 'Email') & (marketing[segment] == subsegment)]

      subscribers = email.groupby(['user_id', 'variant'])['converted'].max()
      subscribers = pd.DataFrame(subscribers.unstack(level=1)) 
      control = subscribers['control'].dropna()
      personalization = subscribers['personalization'].dropna()

      print('lift:', lift(control, personalization))
      print('t-statistic:', stats.ttest_ind(control, personalization), '\n\n')

ab_segmentation('language_displayed')
ab_segmentation('age_group')
