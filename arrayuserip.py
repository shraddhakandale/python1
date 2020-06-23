from array import *

arr = array('i', [])
n = int(input("enter the size of array"))
for i in range(n):
    x = int(input("enter the next value"))
    arr.append(x)
def sum(arr1):
    add = 0
    for i in arr1:
        add = add+i
    return add
print(sum(arr))


# print(arr)
# print(sorted(arr))
# data = int(input("enter the value to search"))
# index = 0
# for i in arr:
#     if i == data:
#         print('required value is at index',index)
#         break
#     index = index+1
# print(arr.index(data)) # function to find index


# arr = array('i', [])
# n = int(input("enter the size of array"))
# for i in range(n):
#     x = int(input("enter the next value"))
#     arr.append(x)
# delete = int(input("enter the number you want to delete"))
# arr2 = array('i', [])
# for element in arr:
#     if delete == element:
#         continue
#     arr2.append(element)
# print(arr2)

arr1 = array('i', [])
n = int(input("enter the size of array"))
for i in range(n):
    val = int(input("enter the next value"))
    arr1.append(val)
arr2 = array(arr1.typecode, (a for a in arr1))
print(arr2)
counter = len(arr1)-1
for i in arr1:
    arr2[counter] = i
    counter = counter-1
print(arr2)
print(arr2[1])

