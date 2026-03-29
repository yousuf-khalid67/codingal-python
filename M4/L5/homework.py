class BMW:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"BMW {self.model} engine started with a smooth sound"
    
    def accelerate(self):
        return f"BMW {self.model} accelerates smoothly"
    
    def stop_engine(self):
        return f"BMW {self.model} engine stopped"


class Ferrari:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    
    def start_engine(self):
        return f"Ferrari {self.model} engine roared to life"
    
    def accelerate(self):
        return f"Ferrari {self.model} accelerates with incredible speed"
    
    def stop_engine(self):
        return f"Ferrari {self.model} engine turned off"


# Polymorphism demo
cars = [BMW("X5", 2023), Ferrari("F8", 2023)]

for car in cars:
    print(car.start_engine())
    print(car.accelerate())
    print(car.stop_engine())
    print()