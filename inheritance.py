class parent:
    def feature1(self):
        print('feature 1 working')

    def feature2(self):
        print('feature 2 working')


class child(parent):
    def feature3(self):
        print('feature 3 working')

    def feature4(self):
        print('feature 4 working')

class child2(child):
    def feature5(self):
        print('feature 5 working')



p1 = parent()
p1.feature1()
p1.feature2()
print('****************************************************')
c1 = child()
c1.feature3()
c1.feature4()
c1.feature1()
print('****************************************************')
c2 = child2()
c2.feature5()
c2.feature1()
c2.feature4()
