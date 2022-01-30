# CS 4050
# Homework 1 Graphs
# Ryan Christopher

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# data1.txt
# X = 2
# # value 19
# Y = 3.710999997565523
# plt.scatter(X, Y)
# # value 225
# Y = 7.124399999156594
# plt.scatter(X, Y)
# # value 705
# Y = 9.210800024447963
# plt.scatter(X, Y)

# # data2.txt
# X = 3
# # value 128
# Y = 5.337500013411045
# plt.scatter(X, Y)
# # value 5756
# Y = 6.731899979058653
# plt.scatter(X, Y)
# # value 9982
# Y = 6.823100004112348
# plt.scatter(X, Y)

# # data3.txt
# X = 4
# # value 1997
# Y = 10.722000006353483
# plt.scatter(X, Y)
# # value 20680
# Y = 9.312599984696135 
# plt.scatter(X, Y)
# # value 23887
# Y = 11.721499991836026
# plt.scatter(X, Y)

# # data4.txt
# X = 5
# # value 68189
# Y = 32.35559997847304
# plt.scatter(X, Y)
# # value 921111
# Y = 34.17219998664223 
# plt.scatter(X, Y)
# # value 945099
# Y = 36.92770001362078
# plt.scatter(X, Y)

# data = pd.read_csv('data.csv')
# print(data)
# dict = [{2: 3.710999997565523, 2: 7.124399999156594, 2: 9.210800024447963, 3: 5.337500013411045, 3: 6.731899979058653, 3: 6.823100004112348, 4: 10.722000006353483, 4: 9.312599984696135, 4: 11.721499991836026, 5: 32.35559997847304, 5: 34.17219998664223, 5: 36.92770001362078}]

# data = pd.DataFrame(dict)
# X = data.iloc[[0]]
# Y = data.iloc[[1]]
X = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
Y = [3.710999997565523, 7.124399999156594, 9.210800024447963, 
    5.337500013411045, 6.731899979058653, 6.823100004112348, 
    10.722000006353483, 9.312599984696135, 11.721499991836026,
    32.35559997847304, 34.17219998664223, 36.92770001362078]

plt.scatter(X, Y)

# Building the model
X_mean = np.mean(X)
Y_mean = np.mean(Y)

num = 0
den = 0
for i in range(len(X)):
    num += (X[i] - X_mean)*(Y[i] - Y_mean)
    den += (X[i] - X_mean)**2
m = num / den
c = Y_mean - m*X_mean

#print (m, c)

# Linear Regression Line
predY = []
for val in X:
    predY.append(m*val + c)
#predY = m*X + c

plt.plot([min(X), max(X)], [min(predY), max(predY)], color='red')

plt.show()