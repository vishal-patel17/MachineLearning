# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:57:56 2018

@author: vp185104
"""

import math

# print("Value of pi is %5.2f." % math.pi)

#squares = []
### x still exists outside of the loop
# for x in range(10):
#     squares.append(x**2)
# print(squares)

# List comprehension: 
squares = [x**2 for x in range(10)]

# print(squares)

a = [(x,y) for x in [1,2,3] for y in [4,3,1] if x!=y]
# print(a)

# Transpose rows and columns
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
# print(matrix)

# print([[row[i] for row in matrix] for i in range(4)])

b = [-1,0,1,2,3,4,5,6,7,8,9]
# del b[0]
del b
b = 12
print(b)