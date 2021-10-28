import numpy as np
import array
# Aggregations: min, max, etc.
# when facing large amounts of data first step should be summary statistics
# Summing the values in an array
L = np.random.random(100)
sum(L)
# results are the same as np.sum(x)
np.sum(L)
big_array = np.random.rand(1000000)
%timeit sum(big_array)
%timeit np.sum(big_array)
# Because it executes the operation in compiled code, numpy's version is much quicker
# sum function and np.sum function are not identical!!!
# python has built-in min and max functions
min(big_array), max(big_array)
# numpys functions have similar syntax and operate much quicker
np.min(big_array), np.max(big_array)
%timeit min(big_array)
%timeit np.min(big_array)
# for min, max, sum, and other numpy aggregates, a shorter syntax is to use
# methods of the array object itself
print(big)
print(big_array.min(), big_array.max(), big_array.sum())
# whenever possible make sure to use numpy version when operating on numpy arrays
#######
# multidimensional aggregates 
# one common type of aggregate is an aggregate along a row or column
# if you have data stored in a two dimensional array:
M = np.random.random((3,4))
print(M)
# by default each numpy aggregation function will return the aggregate over the entire array:
M.sum()
# aggregations functions take an additional argument specifying the axis where the aggregate is computed
# can specify with (axis=0)
M.min(axis=0)
# The function returns four values, corresponding to the four columns of numbers.
# we can find the maximun value with each row:
M.max(axis=1)
# specifying axis=0 means that the first axis will be collapsed: for two dimensional arrays, 
# this means that values within each column will be aggregated
!head -4 president_heights.csv
import pandas as pd
data = pd.read_csv('president_heights.csv')
heights = np.arrays(data['height(cm)'])
print(heights)
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)
# had to download the complete file ^^
print("Mean height:     ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())
# in each case the aggregation operation reduced the entire array to a single summarizing
# value, which gives us information about the distribution of values
print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))
# sometimes it's more useful to see a visual representation of this data, we can do this using matplotib
import matplotlib.pyplot as plt
import seaborn; seaborn.set() # set plot style
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylable('number'):
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylable('number');
plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number');
plt.hist(heights)

