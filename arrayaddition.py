from numpy import *

# arr = array([1,2,3,4,5])
# arr = arr+5
# print(arr)

# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,2])
# arr3 = arr1+arr2
# print(arr3)

# arr1 = array([1,2,3,4,5])
# print(sum(arr1))
# print(sin(arr1))
# print(cos(arr1))
# print(min(arr1))
# print(max(arr1))
# print(sqrt(arr1))
# arr2 = array([12,14,15,16,13])
# print(concatenate([arr1,arr2]))

# arr1 = array([1,2,3,5,6])
# arr2 = arr1
# print(arr1)
# print(arr2)
# print(id(arr1))
# print(id(arr2))
# arr3 = arr1.view() # shallow copy data from one array to another means both the arrays are still dependent on each other
# print(arr3)
# print(id(arr3))
# arr1[1] = 4
# print(arr1)
# print(arr3)
# arr4 = arr1.copy() # deep copy independent two arrays if you change data in one array other array wont be affected
# print(arr4)
# arr1[1] = 3
# print(arr1)
# print(arr4)

# arr1 = array([1, 2, 3, 4, 5])
# arr2 = array([2, 5, 4, 6, 9])
# arr3 = empty(5,int)
# for i in range(len(arr1)):
#     arr3[i]=arr1[i]+arr2[i]
# print(arr3)

arr = array([1,2,4,6,89])
max=0
for i in range(len(arr)):

    if max < arr[i]:
        max = arr[i]

print('max value is', max)


