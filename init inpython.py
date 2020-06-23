class computer:
    def __init__(self, cpu, ram):
        self.c = cpu
        self.r = ram

    def config(self):
        print("config is :",self.c,self.r)


comp1 = computer("i5",16)
comp2 = computer("i3",8)
comp1.config()
comp2.config()
