class YamahaR7:
    category = "motorcycle"

    def __init__(self, model_name, year, color, top_speed):
        self.model_name = model_name
        self.year = year
        self.color = color
        self.top_speed = top_speed

    def display(self):
        print(f"{self.model_name} ({self.year}) is {self.color} and has a top speed of {self.top_speed}.")

r7 = YamahaR7("Yamaha R7", "2023", "blue", "139 mph")
r7.display()