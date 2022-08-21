# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:30:19 2021

@author: User
"""

import pandas as pd
from sklearn import linear_model

df=pd.read_excel("I:\\advanced analytics\Data_Files\Employee Salaries.xlsx",header=2)

reg=linear_model.LinearRegression()
MBA = {'No': 0,'Yes': 1} 
df.MBA = [MBA[item] for item in df.MBA] 
reg.fit(df[['Age','MBA']].values,df[['Salary']])
print(df)
print(reg.coef_)
print(reg.intercept_)

df["Interaction"]=df["Age"]*df["MBA"]
print(df)

reg.fit(df[['Age','MBA','Interaction']].values,df[['Salary']])
print(reg.coef_)
print(reg.intercept_)

reg.fit(df[['Age','Interaction']].values,df[['Salary']])
print(reg.coef_)
print(reg.intercept_)
