# method resolution order from left to right
class parent1:
    def __init__(self):
        print("in parent1 init")

    def feature1(self):
        print("in parent1-feature1")


class parent2:
    def __init__(self):
        print("in parent2 init")

    def feature1(self):
        print("in parent2-feature1")


class child(parent1, parent2):
    def __init__(self):
        super().__init__()
        print("in child init")

    def feature2(self):
        super().feature1()   # by using super keyword we can call not only init method but other methods also.


c = child()  # object of child class
c.feature2()
