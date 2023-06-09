import numpy as np

# For numpy to work u need to install anaconda which is a package manager
# numpy makes it easier to do element wise operations
a = [1, 2, 3, 4, 5]

b = [i**2 for i in a]

print("Squaring the array => ", b)

c = np.array([1, 2, 3, 4, 5])

print("Squaring the array using np.array => ", c**2)

d = range(100000)

e = [i**2 for i in d]

print("Using timeit to check time taken to evaluate a numpy operation")
# %timeit [i**2 for i in d]

f = c*2
print("Multiplying the array using np.array => ", f)

print("To check dimensions of an array use ndim", c.ndim)

# shape returns a tuple for ex a double dimension array with 8 elements in x row and 2 elements in y row will return (8,2)
print("To check elements as per dimensions of an array use shape", c.shape)

arange = np.arange(0, 9)
print("To generate a list of numbers from a to b use arange(a,b) ", arange)

arange1 = np.arange(0, 9, 2)
print("To generate a list of numbers from a to b use arange with step x use arange(a,b,x) ", arange1)

linespace = np.linspace(0,2,9)
print("To generate n numbers between a and b use linespace(a,b,n) ", linespace)

print("To check type of an array u can use type(arr) ", type(arange))