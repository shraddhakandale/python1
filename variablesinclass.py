class car:
    wheels = 4  # class variable

    def __init__(self):
        self.com = "BMW"  # instance variables
        self.mil = 10


c1 = car()
c2 = car()
c1.mil = 8
car.wheels = 5
print("com :",c1.com ,"," "milage :",c1.mil ,"," "wheels :",c1.wheels)
print("com :",c2.com ,"," "milage :",c2.mil ,"," "wheels :", c2.wheels)

