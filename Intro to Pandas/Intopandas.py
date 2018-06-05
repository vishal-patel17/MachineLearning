# -*- coding: utf-8 -*-
"""
Created on Sun May 20 20:56:17 2018

@author: vp185104
"""

import pandas as pd
import numpy as np

# print(pd.__version__)

numbers = pd.Series(['One', 'Two', 'Three', 'Four'])
# print(numbers)

letters = pd.Series(['A', 'B', 'C'])

population = pd.Series([1234, 56789, 890988])

result = pd.DataFrame({'Numbers': numbers, 'Letters':letters})
# print(result)

# data = pd.read_csv('sampleData.csv', sep=",")
# desc = data.describe()
# head = data.head()

# hist = data.hist('total_bedrooms')

# print(type(numbers[:2]))
# print(letters * 2)

# np.log(letters) #error

print(population.apply(lambda val: val > 2000))
