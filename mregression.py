# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 15:32:08 2020

@author: swapnil
"""

import pandas as pd
from sklearn import linear_model
df=pd.read_excel("I:\\advanced analytics\Data_Files\Colleges and Universities.xlsx",header=2)
print(df.columns)

mlr=linear_model.LinearRegression()
mlr.fit(df[['Median SAT', 'Acceptance Rate',
       'Expenditures/Student', 'Top 10% HS']],df[['Graduation %']])
print(mlr.coef_)
print(mlr.intercept_)
print(mlr.predict([[1315,.22,26636,85]]))