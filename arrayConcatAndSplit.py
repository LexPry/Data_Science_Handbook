import numpy as np
import array
# Array concatenation and splitting
# primarily accomplished through np.concatenate, np.vstack, and np.hstack
# np.concatenate make a tuple or list of arrays as its first argument
x = np.array([1,2,3])
y = np.array([3,2,1])
np.concatenate([x,y])
# can also concatenate more than two arrays at once:
z = [99,99,99]
print(np.concatenate([x,y,z]))
grid = np.array([[1,2,3],[4,5,6]])
# concatenate along the first axis
np.concatenate([grid, grid])
# concatenate along the second axis (zero-indexed)
np.concatenate([grid, grid], axis = 1)
# For working with arrays of mixed dimensions, it can be clearer to use the np.vstack and np.hstack
# functions
x = np.array([1,2,3])
grid = np.array([[9,8,7],
[6,5,4]])
x = np.array([1,2,3])
grid = np.array([[9,8,7],
[6,5,4]])

# vertically stack the arrays
x = np.array([1,2,3])
grid = np.array([[9,8,7],
[6,5,4]])

# vertically stack the arrays
np.vstack([x, grid])
# horizontally stack the arrays
y = np.array([[99],
             [99]])
np.hstack([grid, y])
# Splitting of arrays
# The opposit of concatenation is splitting, implemented by the functions np.split, and np.hsplit
x = [1,2,3,99,99,3,2,1]
x1,x2,x3 = np.split(x, [3,5])
pint(x1,x2,x3)
x = [1,2,3,99,99,3,2,1]
x1,x2,x3 = np.split(x, [3,5])
print(x1,x2,x3)
# N split points lead to N + 1 subarrays. The related function np.hsplit and np.vsplit
# are similar
grid = np.arange(16).reshape((4,4))
grid
upper, lower = np.vsplit(grid, [2])
print(upper)
print(lower)
left, right = np.hsplit(grid, [2])
print(left)
print(right)
# similarly, np.dsplit will split arrays along the third axis

