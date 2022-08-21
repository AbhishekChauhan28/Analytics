# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:13:56 2020

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df=pd.read_excel("I:\\advanced analytics\Data_Files\Purchase Orders.xlsx", skiprows=2)
##restrict maximum number of columns to be printed
pd.set_option('display.max_columns',5)

#print(df[["Supplier ", "Cost per order"]].sort_values(["Supplier ", "Cost per order"]))

print (df)

##tyoe of df
print(type(df))

##display first five records
print (df.head(5))

##display last three records
print (df.tail(3))

##name of the attributes

print(df.columns)
print(df.shape)
print(df.info)
##number of rows in the data frame
print(len(df))

#Frequency distribution of categorical variable
print(df.sort_values(["Supplier ", "Cost per order"]))

freq_dist=df["Item Description"].value_counts().sort_index()
print(freq_dist)
print(freq_dist.index.tolist())
print(freq_dist.tolist())
print(freq_dist.axes)

#Plot frequency distribution of categorical variable
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(freq_dist.index.tolist(),freq_dist.tolist())
plt.xticks(rotation=90)
plt.ylabel('Frequency')
plt.xlabel('Item Name')
plt.title('Frequency Distribution for Purchase Order Items')
plt.show()

#Relative frequency distribution and cumulative frequency distribution
freq_dist_df=freq_dist.to_frame().reset_index()
print(freq_dist_df)
print(freq_dist_df[freq_dist_df.columns[1]])
count=len(df)
freq_dist_df["Relative Frequency"]= freq_dist_df[freq_dist_df.columns[1]]/count
freq_dist_df['Cumulative Frequency'] = freq_dist_df["Relative Frequency"].cumsum()
plt.show()
print(freq_dist_df)

#frequency distribution of continuous variable
#plt.hist(df["A/P Terms (Months)"])
plt.hist(df["Cost per order"],bins=10)
plt.ylabel('Frequency')
plt.xlabel('Cost per order')
#plt.xlabel('A/P Terms')
plt.title('Histogram')
plt.show()

print(df["A/P Terms (Months)"].value_counts())

plt.hist(df['Cost per order'],bins=10)
plt.ylabel('Frequency')
plt.xlabel('Cost per Order')
plt.title('Histogram')
plt.hist(df['Cost per order'],bins=10, cumulative=True)

#percentile
print("Percentile of score ", stats.percentileofscore(df['Cost per order'],20000))
print("Score at Percentile", stats.scoreatpercentile(df['Cost per order'],90))

# quartiles
print("Quartiles ", np.percentile(df['Cost per order'], np.arange(0, 100, 25)) )

# deciles
print(np.percentile(df['Cost per order'], np.arange(0, 100, 10)))

#Cross Tabulation
print(pd.crosstab(df["A/P Terms (Months)"],df["Item Description"]))

#Sorting
print(df[["Supplier ", "Cost per order"]].sort_values(["Supplier ", "Cost per order"]))

#Group by and aggregate
print(df.groupby("Supplier ")["Cost per order"].mean())
print(df.groupby("Supplier ")["Cost per order"].mean().reset_index())
print(df.groupby("Supplier ")["Cost per order"].max().reset_index())

#Filtering
print(df[df["Item Cost"]>=200][["Order No.","Item Cost"]])

#Joining of data frames
supplier_cost_mean=df.groupby("Supplier ")["Cost per order"].mean().reset_index()
supplier_cost_max=df.groupby("Supplier ")["Cost per order"].max().reset_index()
supplier_cost_summary=supplier_cost_mean.merge(supplier_cost_max,on="Supplier ")
print(supplier_cost_summary)
