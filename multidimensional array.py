from numpy import *

# arr = array([1,2,3,4,5], int)
# print(arr)

# ways of creating array using numpy
# 1.array() 2.linspace() 3.logspace() 4.arange() 5.zeros() 6.ones()

# arr = array([1, 2, 3, 4, 5], float)
# print(arr)
# print(arr.dtype)

# arr = linspace(0,10,5) # divide the numbers from 0 to 10 in 5 parts
# print(arr)

# arr = arange(1,15,2) # skip 2 number
# print(arr)

arr = logspace(1,40,5) # divide the number from 10^1 to 10^40 into 5 parts
print('%.2f'%arr[4]) # two digits after decimal point

arr = zeros(5, int)
arr2 = ones(5, int)
print(arr)
print(arr2)

