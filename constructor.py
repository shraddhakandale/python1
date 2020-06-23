class computer:
    def __init__(self):
        self.name = "shraddha"
        self.age = 20

    def update(self):
        self.age = 18

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()

c1.update()
print(c1.name)
print(c2.name)
print("age of c1 is :", c1.age)
print("age of c2 is :", c2.age)

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")
