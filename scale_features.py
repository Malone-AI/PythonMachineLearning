"""
特征缩放
"""
import pandas as pd
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler 
scale = StandardScaler()

df = pd.read_csv("Machine_learning_tutorial/cars.csv")

X = df[['Weight', 'Volume']]
y = df["CO2"]
X = X.values
y = y.values

scaledX = scale.fit_transform(X)

regr = linear_model.LinearRegression()
regr.fit(scaledX,y)

scaled = scale.transform([[2300,1300]])
predictCO2 = regr.predict([scaled[0]])

print(predictCO2)