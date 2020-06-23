# array in python
# unsigned int I : only positive int values
# signed int i:positive and negative int values
# float f
# double d
#signed long l
#unsigned lonh L

from array import *
vals = array('i', [5,9,-8,4,2])
# newarr = array(vals.typecode, (a*a for a in vals))
# vals.reverse()
# for i in vals:
#     print(i)
# for i in range(len(newarr)):
#     print(newarr[i])
# i=0
# while i<len(newarr):
#     print(newarr[i])
#     i=i+1
print(sorted(vals))


# vals = array('u', ['a','e','i','o','u'])
# for i in vals:
#     print(i)
