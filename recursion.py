# function calling itself
import sys

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i = 0
def greet():
    global i
    i+=1
    print("Hello", i)
    greet() # bydefault recursion can be called 1000 times


greet()