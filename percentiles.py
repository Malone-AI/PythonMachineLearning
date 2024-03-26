"""
百分位数
"""
import numpy as np
ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
print(f"75th percentile = {np.percentile(ages,75)}")
print(f"90th percentile = {np.percentile(ages,90)}")
print(f"50th percentile = {np.percentile(ages,50)}")#等价于中位数
print(f"median = {np.median(ages)}")