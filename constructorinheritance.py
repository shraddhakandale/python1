class parent:
    def __init__(self):
        print("in parent init")

    def feature1(self):
        print('feature 1 is working')

class child(parent):

    def __init__(self):
        super().__init__()
        print("in child init")

    def feature2(self):
        print('feature 2 is working')
print("object of parent class")
p = parent()
print("object of child class")
c = child()

