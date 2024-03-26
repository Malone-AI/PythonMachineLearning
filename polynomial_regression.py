"""
多项式回归
"""
import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import r2_score

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

mymodel = np.poly1d(np.polyfit(x,y,3))
myline = np.linspace(1,22,100)
r_square = r2_score(y,mymodel(x))
print(f"r_square = {r_square}")
y_hat = mymodel(17)
print(f"When it is 17:00 , the speed is {y_hat}")

plt.scatter(x,y)
plt.plot(myline,mymodel(myline))
plt.show()

