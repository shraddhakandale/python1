class pycharm:
    def execute(self):
        print('compiling')
        print("running")
class Myeditor:
    def execute(self):
        print("spell check")
        print('compiling')
        print("running")

class laptop:
    def code(self, ide):
        ide.execute()


ide1 = Myeditor()
lap1 = laptop()
lap1.code(ide1)
