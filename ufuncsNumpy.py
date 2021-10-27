import numpy as np
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output
    
values = np.random.randint(1,10, size=5)
compute_reciprocals(values)
# shows the slowness of loops when computing the values of the reciprocal of each
big_array = np.random.randit(1, 100, size 1000000)
%timeit compute_reciprocals(big_array)
big_array = np.random.randit(1, 100, size=1000000)
%timeit compute_reciprocals(big_array)
big_array = np.random.randint(1, 100, size=1000000)
%timeit compute_reciprocals(big_array)
print(compute_recipricals(values))
print(1.0 / values)
print(compute_reciprocals(values))
print(1.0 / values)
# big array completes orders of magnitude faster than the python loop
%timeit (1.0 / big_array)
np.arange(5)/np.arange(1,6)
# ufunc operations are not limited to one-dimensional arrays- they can act on multidim arrs too
x = np.arange(9).reshape((3,3))
2 ** x
# Ufuncs exist as unary ufuncs which operate on a single input
# and binary ufuncs which operate on two inputs
# Array arithmetic feels natural because of pythons native arithmetic operators
x = np.arange(4)
print("x    =", x)
print("x + 5 =", x+5)
print("x - 5 =", x-5)
print("x*2 =", x * 2)
print("x / 2 =", x / 2)
print("x // 2 =", x // 2)
# // represents floor division
# ** operator for exponentation, and a % for modulus
print("-x   =", -x)
print("x ** 2 =", x ** 2)
print("x % 2 =", x % 2)
# can be strung together however and order of operations is respected
-(0.5*x +1) ** 2
# absolute value, numpy understands python's built in arithmetic operators
x = np.array([-2, -1, 0, 1, 2])
abs(x)
# The corresponding numpy function is np.absolute (alias = np.abs)
np.absolute(x)
np.abs(x)
# can also handle complex data, in which the absolute value returns magnitude
x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
np.abs(x)
# trigonometric functions are available under numpy
theta = np.linspace(0, np.pi, 3)
# can compute trigonometric functions
print("theta   =", theta)
print("sin(theta) =", np.sin(theta))
print("cos(theta) =", np.cos(theta))
print("tan(theta) =", np.tan(theta))
# inverse trigonometric functions are available also
x = [-1, 0, 1]
print("x     =",x)
print("arcsin(x) = ", np.arcsin(x))
print("arccos(x) = ", np.arccos(x))
print("artan(x) = ", np.arctan(x))

