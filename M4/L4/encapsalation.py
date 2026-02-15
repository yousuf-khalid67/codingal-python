class Computer:
    _ramstorage=16
    def __init__(self):
        self._maxprice=10000
    def display(self):
        print(self._maxprice)
        print(self._ramstorage)
    def _updateprice(self, newprice):
        self._maxprice=newprice

c1=Computer()
c1.display()
print(c1._maxprice)
print(c1._ramstorage)
c1._updateprice(1000000)
c1.display()
