"""
拆分训练集和测试集
"""
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
np.random.seed(2)

x = np.random.normal(3,1,100)
y = np.random.normal(150,40,100)/x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = np.poly1d(np.polyfit(train_x,train_y,4))
myline = np.linspace(0,6,100)

r_square_train = r2_score(train_y,mymodel(train_x))
print(f"In train set , r_square = {r_square_train}")
r_square_test = r2_score(test_y,mymodel(test_x))
print(f"In test set , r_square = {r_square_test}")

print(mymodel(5))

plt.scatter(train_x,train_y)
plt.plot(myline,mymodel(myline))
plt.show()