import numpy as np
import os
import random
"""
    To prepare the data intended for building graphs, the following steps need to be taken:
    
    1. The formula used: theta = (N1 + N2 + (N2 // m - 1) * n) * sigma;
        1.1. Known constants: 
            theta = 6 
            m = 1
            n = 9
            sigma = 0.01 ... 0.1
            N1 + N2 = 60 
            N2 = 0 ... 59 -> N1 = 60 ... 1
        1.2. Transform the formula using known data:
            sigma = theta / (N1 + N2 + (N2 // m - 1) * n)  
    2. Exclude boundary cases and fix all the required values ​​immediately: 
        2.1 sigma = 0.01, N1 = 1, N2 = 59, n = 9, m = 1 -> side chains fill each segment
        2.2 sigma = 0.1, N1 = 60, N2 = 0, n = 0, m = 1 -> only backbone without side chains
        
    3. Необходимые графики для статьи:
    0 (N1 = 60, N2 = 0) (60)- 25 (N1 = 45, N2 = 15) (45)- 50 (N1 = 30, N2 = 30) (30)- 75 (N1 = 15, N2 = 45) (15)- 1 (N1 = 1, N2 = 59) (1)
"""

# Known variables and constants
theta = 6.0
m = 1.0
n = 9

label1 = True
if os.path.exists('results.txt') == label1:
    os.remove('results.txt')
    label1 == False
else:
    label1 == label1
ans = [0.01]    
with open('results.txt', 'a') as file1:
        file1.writelines(
            'sigma = 0.01, N1 = 1, N2 = 59, n = 9, m = 1'+'\n')
# A loop for finding n for each value of sigma and N
for i in range(58, 0, -1):  # over a range of N2 values
    sigma = theta / (60 + (i // m - 1) * n) 
    ans.append(sigma)


    with open('results.txt', 'a') as file1:
        file1.writelines(
            f'sigma = {sigma}, N1 = {60-i}, N2 = {i}, n = {n}, m = 1'+'\n')