# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:50:01 2021

@author: User
"""

import pandas as pd
from sklearn import linear_model

df=pd.read_excel("I:\\advanced analytics\Data_Files\Surface Finish.xlsx",header=2)
print(df)
df1=pd.concat([df,pd.get_dummies(df["Cutting Tool"])],axis=1)
print(df1)
reg=linear_model.LinearRegression()

reg.fit(df1[['RPM','B','C','D']].values,df1[['Surface Finish']])
print(reg.coef_)
print(reg.intercept_)
