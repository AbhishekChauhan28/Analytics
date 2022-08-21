# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:14:48 2020

@author: swapnil
"""

import pandas as pd
from scipy.stats import f_oneway

df=pd.read_excel("I:\\advanced analytics\Data_Files\Insurance Survey.xlsx", skiprows=2, nrows=24)
print(df.columns)

df1=df.loc[df["Education"]=="Some college"]["Satisfaction* "]
print(df1)
df2=df.loc[df["Education"]=="Graduate degree"]["Satisfaction* "]
print(df2)
df3=df.loc[df["Education"]=="College graduate"]["Satisfaction* "]
print(df3)
print(f_oneway(df1,df2,df3))