# f = lambda a:a*a
# result = f(int(input("enter number")))
# print(result)

# f = lambda a,b : a+b
# result = f(int(input("enter first number")),int(input("enter second number")))
# print(result)

# def is_even(n):
#     return n%2==0

from functools import reduce
nums = [2,3,6,8,4,6,2,9,7]
# evens = list(filter(is_even,nums))
evens = list(filter(lambda n: n%2==0,nums))
doubleeven = list(map(lambda n: n*2,evens))
sum = reduce(lambda a,b:a+b,doubleeven)
print(evens)
print(doubleeven)
print(sum)
