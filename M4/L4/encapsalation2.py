class Person:
    def __init__(self, age):
        self.__age=age
    
    def display(self):
        print(self.__age)

p1=Person(11)
p1.display()
print(p1.__age)