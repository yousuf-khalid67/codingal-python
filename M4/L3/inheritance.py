class Person:
    def __init__(self, name, age, city, bloodgroup):
        self.name=name
        self.age=age
        self.city=city
        self.bloodgroup=bloodgroup
    def display(self):
        print(self.name, self.age, self.city, self.bloodgroup)

class Employee(Person):
    def __init__(self, name, age, city,bloodgroup, post, salary, department):
        super().__init__(name, age, city, bloodgroup)

        self.post=post
        self.salary=salary
        self.department=department
    def display(self):
        print(self.name, self.age, self.city, self.bloodgroup, self.post, self.salary, self.department)

employee1=Employee("boo", 35,"melbourne","b+", "manager", "$1,000,000,000", "operation")
employee1.display()