import pandas as pd
import matplotlib.pyplot as plt

data_filename = 'Advertising.csv'
df = pd.read_csv(data_filename)

df.head()

df_new = df.iloc[:7]
print(df_new)

# scatter plot for first seven points
plt.scatter(df_new['TV'], df_new['Sales'])

plt.xlabel('TV budget')
plt.ylabel('Sales')

plt.title('Graph of TV Budget vs Sales')

# scatter plot for all points
plt.scatter(df['TV'], df['Sales'])

plt.xlabel('TV budget')
plt.ylabel('Sales')

plt.title('Graph of TV Budget vs Sales')
