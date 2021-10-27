import numpy as np
np.ranom.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # one dimensional array
x2 = np.random.randint(10, size=(3,4)) # Two dimensional array
x3 = np.random.randint(10, size(3,4,5)) # Three dimensional array
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # one dimensional array
x2 = np.random.randint(10, size=(3,4)) # Two dimensional array
x3 = np.random.randint(10, size(3,4,5)) # Three dimensional array
np.random.seed(0) # seed for reproducibility
x1 = np.random.randint(10, size=6) # one dimensional array
x2 = np.random.randint(10, size=(3,4)) # Two dimensional array
x3 = np.random.randint(10, size=(3,4,5)) # Three dimensional array
# each array has attributes ndim, shape, and size
print("x3 ndim: ", x3.ndim)
print("x3 shape: ", x3.shape)
print("x3 size: ", x3.size)
# Other attributes inlcude itemsize, which lists the size (in bytes of each array element)
# and nbytes which lists the total size (in bytes) of the array:
print("itemsize:", x3.itemsize, "bytes")
print("nbytes:", x3.nbytes, "bytes")
# Array indexing: Accessing single elements
x1
x1[0]
x1[4]
#
# To index from the end of the array, you can use negative indicies:
x1[-1]
x1[-2]
x2
x2[0,0]
x2[2,0]
x2[2,-1]
x1[0] = 3.14159 # this will be truncated
x1
x = np.arange(10)
x
x[:5] # first five elements
x[5:] # elements after index 5
x[4:7] #  middle subarray
x[::2] # every other element
x[1::2] # every other element, starting at index 1
x[::-1] # all elements, reversed
x[5::-2] # reversed every other from index 5
x2
x2[:2,:3] # two rows, three columns
x2[:3,::2] # all rows, every other column
x2[::-1,::-1] # subarray dimensions can be reversed together
print(x2[:,0]) # first column of x2
print(x2[0, :]) # first row of x2
print(x2[0]) # equivalent to x2[0, :]
x2[0,0] = 12 # can modify using index notation
x2
# array slices return views rather than copies of the array data
print(x2)
x2_sub = x2[:2,:2] # extract a 2x2 subarray from this
print(x2_sub)
x2_sub[0,0] = 99
print(x2_sub) # the orignal array will change
print(x2)
# copying can be done most easily using the .copy() function
x2_sub_copy = x2[:2,:2].copy()
print(x2_sub_copy)
# now if we modify this subarray, the original array is not touched:
x2_sub_copy[0,0]=42
print(x2_sub_copy)
print(x2)
# Reshaping of arrays using the reshape() method
# if you want to put the numers 1 through 9 in a 3x3 grid you can do:
grid = np.arange(1,10.reshape((3,3))
print(grid)
# Reshaping of arrays using the reshape() method
# if you want to put the numers 1 through 9 in a 3x3 grid you can do:
grid = np.arange(1,10).reshape((3,3))
print(grid)
# for this to work the size of the intial array must match the size of the reshaped array
# another reshaping patter is the conversino of a one dimensional array into a two dimensional row 
# or column matix by making use of the newaxis keyword within slice operation
x = np.array([1,2,3])
# row vector via reshape
x.reshape((1,3))
# row vector via newaxis
x[np.newaxis, :]
# column vector via reshape
x.reshape((3,1))
# column vector via newaxis
x[:,np.newaxis]

