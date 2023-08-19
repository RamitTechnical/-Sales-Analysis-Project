import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from collections import Counter
df = pd.read_csv('Cleaned_combined_data.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 1. What was the best month for sales? How much was earned that month?
# sales
# month

df['sales'] = df['Price Each']*df['Quantity Ordered']
df['month'] = df['Order Date'].dt.month_name()
gdf = df.groupby('month')['sales'].sum().reset_index()

# sns.catplot(x='month', y='sales', data=gdf, kind='bar')
# plt.show()
#print(gdf)
# 2. What city sold the most product?
# 3 task What city sells the most product in quantity
# city
# "917 1st St, Dallas, TX 75001"
# str.split(',')[1]
df['city'] = df['Purchase Address'].str.split(',', expand=True)[1]
gdf = df.groupby('city')['sales'].sum().reset_index()
#gdf=gdf.sort_values('sales',ascending=False) or gdf=gdf['sales'].max()
#sns.catplot(x='city', y='sales', data=gdf, kind='bar')
# plt.show()
#print(gdf)



#3. What time should we display advertisemens to maximize the likelihood of customer’s buying product?
# hour
df['hour'] = df['Order Date'].dt.hour
gdf = df.groupby('hour')['Quantity Ordered'].sum().reset_index()
# print(gdf)
# sns.catplot(x='hour', y='Quantity Ordered', data=gdf, kind='bar')
# plt.show()

# What products are most often sold together?
df = df.loc[df['Order ID'].duplicated(keep=False)]
df['grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
count = Counter()
row_list = []
for row in df['grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list, 3)))
print(count.most_common(10))