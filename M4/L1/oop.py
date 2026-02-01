class Goats:
    species="animal"
    def __init__(self, name, age, smell, behaviour):
        self.name=name
        self.age=age
        self.smell=smell
        self.behviour=behaviour
    def display(self):
        print(f"{self.name} is {self.age} old, smells {self.smell} and behaves really {self.behviour}")

ozwald=Goats("Ozwald", "4 months", "good", "naughty")
ozwald.display()