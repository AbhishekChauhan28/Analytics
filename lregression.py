# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:48:54 2020

@author: swapnil
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import statsmodels.api as sm

df=pd.read_excel("I:\\advanced analytics\Data_Files\Home Market Value.xlsx",header=2)
print(df)
plt.title('Home Market Value')
plt.xlabel('Area in Square Feet')
plt.ylabel('Market Value in $')
plt.scatter(df['Square Feet'],df['Market Value'],color='red',marker='+')
plt.show()

print(type(df['Square Feet'].values[1]))
reg=linear_model.LinearRegression()
reg.fit(df[['Square Feet']].values,df[['Market Value']])
print("Coefficient,", reg.coef_)
print("Intercept ",reg.intercept_)
print(reg.predict([[1800]]))



plt.plot(df['Square Feet'],reg.predict(df[['Square Feet']]),color='blue')
model=sm.OLS(df['Market Value'],df['Square Feet']).fit()
print(model.summary2())

#pdf=pd.read_csv("F:\python\HMV Prediction.csv")
#mprice=reg.predict(pdf)
#pdf['Market Price']=mprice
#print(pdf)
#pdf.to_csv("F:\python\HMV Prediction.csv",index=False)




