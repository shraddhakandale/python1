# a = 10 # global variable


# def something():
#    a = 15 # local variable
#    print("in function :", a)


# print("outside :", a)
# something()

# a = 10


# def something():
#     global a
#     a = 15
#     print("in function :", a)

# something()
# print("outside :", a)

a = 10
print(id(a))

def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("in function :", a)
    globals()['a'] = 15

something()
print("outside :", a)





