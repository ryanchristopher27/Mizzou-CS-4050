# CS 4050
# Homework 1 Graphs
# Ryan Christopher

# Code references from: 
# https://towardsdatascience.com/linear-regression-using-least-squares-a4c3456e8570

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)


plt.xlabel("Input Size (log10)")

# Algorithm Time
# X = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
# Y = [3.2217999978456646, 6.444300001021475, 8.300800021970645, 
#     4.623900022124872, 5.972200015094131, 5.963800009340048, 
#     6.993400020292029, 5.489499977556989, 8.692000003065914,
#     6.010700017213821, 7.458700012648478, 6.7952999961562455]
# plt.title("Algo_Time vs. Input Size")
# plt.ylabel("Algorithm Time")


# All Time
X = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
Y = [3.710999997565523, 7.124399999156594, 9.210800024447963, 
    5.337500013411045, 6.731899979058653, 6.823100004112348, 
    10.722000006353483, 9.312599984696135, 11.721499991836026,
    32.35559997847304, 34.17219998664223, 36.92770001362078]
plt.title("All_Time vs. Input Size")
plt.ylabel("All Time")

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