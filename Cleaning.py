### Cleaning the data
import pandas as pd
import numpy as np
import os

# path of the sales data
path = r'C:\Users\ramit\Downloads\SalesData'
# getting file names
file_names = os.listdir(path)
# creating single dataframe of complete year sales
fdf = pd.DataFrame()
for fn in file_names:
    df = pd.read_csv(fr'{path}\{fn}')
    fdf = pd.concat([fdf, df])

# original rows and columns ==> [186850 rows x 6 columns]
# Removing mising values

fdf = fdf.dropna()
#print(fdf)

# after removing null values from combined df rows anc cols == > [186305 rows x 6 columns]

#print(fdf.info())
fdf['temp'] = fdf['Order ID'].str.isdigit()
fdf = fdf.loc[fdf['temp'] == True]
fdf['Order ID'] = fdf['Order ID'].astype(np.int64)
fdf = fdf.drop(columns='temp')
fdf.to_csv('Cleaned_combined_data.csv')