# Computation on arrays: broadcasting
# Numpy's universal functions can be used to vectorize operations and remove slow python loops
# another way to vectorize is to use numpy's broadcasting functionality
import numpy as np
a = np.array([0,1,2])
b = np.array([5,5,5])
a + b
# broadcasting allows these types of binary operation to be performed on arrays of different
# sizes, we can easily add a scalar to an array
a + 5
# Think of it like adding [5,5,5] to the array 
# can extend this to arrays of higher dimension
M = np.ones((3,3))
M
M + a
# Here the one-dimensional array is broadcast acros the second dimension to match the shape of M
# We can also do more complicated broadcasts
a = np.arange(3)
b = np.arange(3)[:, np.newaxis]

print(a)
print(b)
a + b
# Rules of Broadcasting: 
# 1: if the two arrays differ in their number of dimensions the shape of the one with fewer dimensions
# is padded with ones on its leading (left) side
# 2: if the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in th# at dimen sion is stretch to match  
# 3: if in any dimension the sizes disagree and neither is equal to 1, and error is raised
# Broadcasting example 1
# Two dimensional array to a one dimensional array
M = np.ones((2,3))
a = np. arange(3)
M + a
# rule 1 the array has fewer dimensions so it's padded on the left with ones -> a.shape(3) -> (1,3)
# rule 2 the first dimension disagrees so we stretch the dimension to match a.shape(2,3)
# the shapes then match and the final shape will be 2,3
# example 2
a = np.arange(3).reshape((3,1))
b = np.arange(3)
# Shape of arrays is:
# a.shape = (3,1)
# b.shape = (3,)
# rule 1: pad
# b.shape -> (1,3) 
# rule 2: upgrade each to match size
# b.shape -> (3,3)
a + b
# example 3:
M = np.ones((3,2))
a = np.arange(3)
# We have to pad the shapes with ones: a.shape -> (1,3)
# Then stretch dimension to match that of M -> (3,3) 
# but rule three states that the shapes are incompatible
M + a
# if you want right side padding you'll have to use the np.newaxis keyword
a[:, np.newaxis].shape
M + a[:, np.newaxis]
# also note that while the + is being focused on, these broadcastin rules apply to any binary ufunc: 
np.logaddexp(M, a[:, np.newaxis])
# Centering an array 
# if you have an array of 10 observation, with 3 values each: 
X = np.random.random((10,3))
# can compute the mean of each feature
Xmean = X.mean(0)
Xmean
# center the x array by subtracting the mean 
x_centered = X - Xmean
# to double check that it's done correctly, we can check that the centered array has a near 0 mean
X_centered.mean(0)
x_centered.mean(0)
# plotting a two-dimensional function
# one place that broadcasting can be useful is in displaying images based on two dimensional functions
# if you want to define z = f(x,y) we can use broadcasting to compute across the grid
# x and y have 50 steps from 0 to 5
x = np.linspace(0,5,50)
y = np.linspace(0,5,50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
%matplotlib inline
import matplotlib.pyplot as plt
plt.imshow(z, origin='lower', extent=[0,5,0,5],cmap='viridis')
plt.colorbar();
%pylab inline
plt.imshow(z, origin='lower', extent=[0,5,0,5],cmap='viridis')
plt.colorbar();
# trying to figure out how to show ^^
import pylab as p
p.show()
plt.imshow(z, origin='lower', extent=[0,5,0,5],cmap='viridis')
plt.colorbar();