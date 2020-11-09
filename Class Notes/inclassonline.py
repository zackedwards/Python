#Author Zack Edwards
#Inclass assignment 3/12

import numpy as np
import pandas as pd

file = 'Regression Data-1.csv'
df1 = pd.read_csv(file)
i = 1
while i < 11:
    t1 = df1['x' + str(i)]
    std = np.std(t1)
    med = np.median(t1)
    print('Average of X' + str(i) , ' is: ', std)
    print('Median of X' + str(i) , ' is: ', med)
    i += 1
