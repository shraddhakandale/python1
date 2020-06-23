class computer:
    def configuration(self):     # method
        print("i5 , 16bit, 1tb")


comp1 = computer() # object
comp2 = computer()
print(type(comp1))
computer.configuration(comp1) # calling
computer.configuration(comp2)
comp1.configuration()
comp2.configuration()

