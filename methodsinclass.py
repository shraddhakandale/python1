class student:
    school = 'abc'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return self.m1 + self.m2 + self.m3 / 3

    @classmethod
    def getschoolname(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is student class...")


s1 = student(10, 56, 89)
s2 = student(20, 12, 36)
print(s1.avg())
print(s2.avg())
print(student.getschoolname())
print(s1.getschoolname())
s1.info()
student.info()
