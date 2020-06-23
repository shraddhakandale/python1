from numpy import *

# arr1 = array([

#     [1,2,3,9,5,7],
#     [4,5,6,12,15,14]


# ])
# print(arr1)
# print(arr1.dtype) # data type
# print(arr1.ndim) # dimension of an array
# print(arr1.shape) # it return a tuple which shows number of rows and columns
# print(arr1.size) # size of the entire array

# arr2 = arr1.flatten() # create 1D array from 2D array
# print(arr2)

# arr3 = arr2.reshape(3,4) # converts 1D array into 2D array of desired number of rows and columns
# print(arr3)
# print("*************************************************************")

# arr4 = arr2.reshape(2,2,3) # converts 1D array into 3D array of  desired number of rows and columns
# print(arr4)

# arr1 = ([
#     [1, 4, 3],
#     [11, 14, 13]
# ])
# m = matrix(arr1)
m1 =  matrix('1,2,3;8 ,4,5;6,7,9')
m2 = matrix('1,5,4;6,8,2;9,7,2')
m3 =m1*m2
print(m1[1][0])
print(m1)
print(m2)
print(m3)
print("diagonal elements are", diagonal(m3))

print('min element is ', m3.min())
