def person(name, **data):  # for keyword var arguments use **
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person("shraddha", age=20, city="latur", mbno=9876543210)
