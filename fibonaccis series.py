# 0 1 1 2 3 5 8 13 21
def fib(n):
    a = 0
    b = 1
    if n<=0:
        print("invalid series")
    elif n==1 :
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            #if c < 100:
            print(c)
fib(int(input("enter number")))