class parent1:
    def feature1(self):
        print("feature 1 is working")


class parent2:
    def feature2(self):
        print("feature 2 is working")


class child(parent1, parent2):
    def feature3(self):
        print("multiple inheritance")
print("parent 1 :")
p1 = parent1()
p1.feature1()
print("parent 2 :")
p2 = parent2()
p2.feature2()
print("child :")
c = child()
c.feature1()
c.feature2()
c.feature3()
