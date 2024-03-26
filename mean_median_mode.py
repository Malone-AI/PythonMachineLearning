"""
平均数、中位数、众数
"""

import numpy as np

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]
print(sorted(speed))
print(f"The length of speed = {len(speed)}")
print(f"mean = {np.mean(speed)}")
print(f"median = {np.median(speed)}")

"""
numpy里没有直接求中位数的方法
故使用scipy.stats
"""
from scipy import stats
x,y = stats.mode(speed)
print(f"mode = {x[0]}")
print(f"frequency = {y[0]}")