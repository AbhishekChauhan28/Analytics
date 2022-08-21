# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 15:47:35 2020

@author: swapnil
"""

import pandas as pd
from scipy import stats

df=pd.read_excel("I:\\advanced analytics\Data_Files\Pile Foundation.xlsx", skiprows=3)
print(df)

print(stats.ttest_rel(df["Estimated"],df["Actual"]))