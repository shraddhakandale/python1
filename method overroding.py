class A:
    def show(self):
        print("in A show")


class B(A):
    def show(self):
        print("in B show")


a1 = B()  # object of class B
a1.show()
