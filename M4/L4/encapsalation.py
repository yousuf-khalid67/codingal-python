class Computer:
    __ramstorage=16
    def __init__(self):
        self.__maxprice=10000
    def display(self):
        print(self.__maxprice)
        print(self.__ramstorage)
    def __updateprice(self, newprice):
        self.__maxprice=newprice

c1=Computer()
c1.display()
print(c1.__maxprice)
print(c1.__ramstorage)
c1.__updateprice(1000000)
c1.display()
