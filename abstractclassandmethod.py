from abc import ABC, abstractmethod


class computer(ABC):
    @abstractmethod
    def process(self):
        pass


class laptop(computer):
    def process(self):
        print("Running...")


class Whiteboard(computer):
    def process(self):
        print("Running in Whiteboard")

    def write(self):
        print("its Writing")


class programmer:
    def work(self, comp):
        print("solving bugs")
        comp.process()


# com = computer()
# com.process()
lap = laptop()
lap.process()
lap2 = Whiteboard()

print('*************************************')
prog1 = programmer()
prog1.work(lap)
prog1.work(lap2)
