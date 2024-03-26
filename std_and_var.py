"""
标准差和方差
"""
import numpy as np
speed = [32,111,138,28,59,77,97]
std = np.std(speed)#求标准差
print(f"standard deviation = {std}")
print(std**2)
var = np.var(speed)#求方差
print(f"var = {var}")
print(var**0.5)