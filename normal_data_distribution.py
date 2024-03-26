"""
正太分布
"""
import numpy as np
from matplotlib import pyplot as plt
x = np.random.normal(5.0,1.0,10000)#生成均值为5.0，标准差为1.0的正太分布数据，共10,000个数据
plt.hist(x,100)
plt.show()