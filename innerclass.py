class student:
    def __init__(self,name,rollno):
        self.name = name
        self.id = rollno
        self.lap = self.laptop() #creating object inside outer class
    def show(self):
        print(self.name, self.id)
        self.lap.show()
    class laptop: #inner class
        def __init__(self):
            self.brand = 'dell'
            self.cpu = 'i5'
            self.ram = 8
        def show(self):
            return print(self.brand,self.cpu,self.ram)

s1 = student('shraddha',22)
s2 = student('saurabh',23)
s1.show()
#lap1 = student.laptop #creating object outside outer class
#print(lap1.brand)