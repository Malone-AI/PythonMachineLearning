"""
多元回归
"""
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("Machine_learning_tutorial/cars.csv")
X = df[['Weight', 'Volume']]
y = df["CO2"]
X = X.values
y = y.values

regr = linear_model.LinearRegression()
regr.fit(X,y)

# 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：
predictCO2 = regr.predict([[2300,1300]])
print(predictCO2)