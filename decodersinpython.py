# def div(a,b):
#     if a<b:
#         a,b=b,a
#     print(a/b)

# div(int(input("enter first number")),int(input("enter second number")))

# using decorators we can add extra features to the existing functions


def div(a, b):
    print(a / b)

def smart_div(func):

    def inner(l,m):
        if l<m:
            l,m = m,l
        return func(l,m)
    return inner

div1  = smart_div(div)

div1(int(input("enter first number")),int(input("entre second number")))
