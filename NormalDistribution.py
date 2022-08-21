# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:04:21 2020

@author: swapnil
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn
from scipy import stats

df=pd.read_excel("I:\\advanced analytics\Data_Files\Purchase Orders.xlsx", skiprows=2)
sbn.distplot(df["Cost per order"], label="Cost per order")
plt.xlabel("Gain")
plt.xlabel("Density")
plt.legend()

#probability of at most 900 F(900)
print(stats.norm.cdf(900,750,100))

#probability of greater than 700 1-F(700)
print(1-stats.norm.cdf(700,750,100))

#probability between 700 and 900 F(900)-F(700)
print(stats.norm.cdf(900,750,100)-stats.norm.cdf(700,750,100))