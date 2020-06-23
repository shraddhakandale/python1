# def person(name,age=18):   #formal arguments
#     print(name)
#     print(age)

# keyword position and default
# person(age=20,name='shraddha')   # actual arguments
# person("shraddha2")

def add(a, *b):  # can have multiple values or def add(*b)

    print(a)
    print(b)
    c = a
    for i in b:
        c = c + i
    print(c)


add(5, 6, 7, 8)
