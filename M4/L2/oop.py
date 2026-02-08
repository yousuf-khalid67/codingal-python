class Employee:
    def __init__(self, name, age, post, salary, department):
        self.name=name
        self.age=age
        self.post=post
        self.salary=salary
        self.department=department
        print("employee object created")
    def __del__(self): 
        print("employee object deleted")
    def display(self):
        print( self.name, self.age, self.post, self.salary, self.department)

employee1=Employee("boo", 35, "manager", "$100,000", "operation")
employee1.display()
del employee1
employee1.display()