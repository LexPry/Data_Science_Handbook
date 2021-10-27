import numpy as np
import array
import arrays
L = lists(range(10))
L
L = list(range(10))
L
type(L[0])
L2 = [str(c) for c in L}
L2 = [str(c) for c in L]
L2
type(L2[0])
L3 = [True, '2', 3.0,4]
[type(item) for item in L3]
L = list(range(10))
A = array.array('i', L)
A
# Here 'i' is type code indicating the contents are integers
# integer array:
np.array([1,4,2,5,3])
# numpy is constrained to arrays of the same type, will upcast if possible if they don't match
np.array([3.14,4,2,3])
np.array([1,2,3,4], dtype='float32')
# use dtype to explicitly set the data type of resulting array
# nested kusts result in multidimensional arrays
np.array([range(i, i + 3) for i in [2,4,6]])
# to create a length-10 integer array filled with zeros
np.zeros(10, dtype=int)
# Create a 3x5 floating-point array filled with 1s
np.ones((3,5), dtype=float)
# create a 3x5 array filled with 3.14
np.full((3,5),3.14)
# Create and array filled with a linear sequence
# Starting at 0, ending at 20, stepping by 2O
# (similar to the built in range() function)
np.arrange(0,20,2)
np.arange(0,20,2)
# Create an array of five values evenly spaced between 0 and 1
np.linespace(0,1,5)
np.linspace(0,1,5)
# Create a 3x3 array of uniformly distributed
# random values between 0 and 1
np.random.random((3,3))
# create a 3X3 array of normally distributed random values with mean 0 and standard deviation 1
np.random.normal(0,1,(3,3))
# To create a 3x3 array of random integers in the interval [0,10]
np.random.randint(0,10,(3,3))
# create 3x3 identity matrix
np.eye(3)
# Create a uninitialized array of three integers the values will be whatever happens to already exist at that memory location
np.empty(3)

