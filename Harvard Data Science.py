# simple data plotting
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


# simple KNN regression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split

filename = 'Advertising.csv'
df_adv = pd.read_csv(filename)

df_adv.head()

# get subset of the data i.e. rows 5 to 13
# use TV column as the predictor
x_true = df_adv.TV.iloc[5:13]

# Use Sales column as the response
y_true = df_adv.Sales.iloc[5:13]

# Sort the data to get indices ordered from lowest to highest TV values
idx = np.argsort(___).values 

# Get the predictor data in the order given by idx above
x_true  = x_true.iloc[idx].values

# Get the response data in the order given by idx above
y_true  = y_true.iloc[idx].values
