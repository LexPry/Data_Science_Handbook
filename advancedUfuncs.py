import numpy as np
x = [1,2,3]
print("x    =",x)
print("e^x  =",np.exp(x))
print("2^x  =",np.exp2(x))
print("3^x  =",np.power(3, ))
x = [1,2,3]
print("x    =",x)
print("e^x  =",np.exp(x))
print("2^x  =",np.exp2(x))
print("3^x  =",np.power(3,x))
# exponents and logarithms
# Logarithms are also available
x = [1,2,4,10]
print("x     =",x)
print("ln(X)  =",np.log(x))
print("log2(x) =",np.log2(x))
print("log10(x) =",np.log(x))
# specialized version useful for maintaining precision with very small input
x = [0,0.001,0.01,0.1]
print("exp(x) - 1=",np.expm1(x))
print("log(1 + x) =",np.log1p(x))
# when x is very small, these functions give more precise values
# Specialized ufuncs
# numpy has hyperbolic trig functions, bitwise arithmetic, comparison operators, conversions from radians # to degress, rounding, remainders,etc
# scipy.special has more specialized and obscure functions
from scipy import special
%pip install scipy
from scipy import special
# Gamma functions (generalized factorials) and related functions
x = [1,5,10]
print("gamma(x)    =",special.gamma(x))
print("ln|gamma(x)| =", special.gammaln(x))
print("beta(x,2)    =", special.beta(x,2))
# error function (integral of Gaussian)
# its complement, and its inverse
x = np.array([0,0.3,0.7,1.0])
print("erf(x)   =", special.erf(x))
print("erfc(x)  =", special.erfc(x))
print("erfinv(x) =", special.erfinv(x))
# Advanced Ufunc Features -> specifying output
# You can specify the array where the result of the calculation will be stored
# For all ufuncs you can do this using the out argument of the functino
# For all ufuncs you can do this using the out argument of the function*
x = np.arange(5)
y = np.empty(5)
np.multiply(x, 10, out=y)
print(y)
# Can be used with array views also
y = np.zeros(10)
np.power(2, x, out=y[::2])
print(y)
# if y[::2] = 2 ** x it would affect memory savings so make sure to plan/think about argument
# Aggregates -> a reduce repeatedly applies a operation to the elements until single result remains
x = np.arange(1, 6)
np.add.reduce(x)
# using reduce on the multiply function returns the product of all elements in array
np.multiply.reduce(x)
np.add.accumulate(x)
# ^ stores all immediate results of computation
np.multiply.accumulate(x)
# any ufunc can compute the output of all pairs of two different input using outer method
x = np.arange(1, 6)
np.multiply.outer(x,x)

