class DogBreed:
    category = "dog"

    def __init__(self, breed_name, origin, size, temperament):
        self.breed_name = breed_name
        self.origin = origin
        self.size = size
        self.temperament = temperament

    def display(self):
        print(f"The {self.breed_name} originated in {self.origin}, is a {self.size} sized dog, and is usually {self.temperament}.")

dog1 = DogBreed("Golden Retriever", "Scotland", "large", "friendly and intelligent")
dog1.display()
