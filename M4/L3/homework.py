class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def display_info(self):
        print(f"Vehicle: {self.name}, Capacity: {self.capacity}")


class Bus(Vehicle):
    def __init__(self, name, capacity, fare_per_km):
        super().__init__(name, capacity)
        self.fare_per_km = fare_per_km
    
    def calculate_total_fare(self, distance, passengers):
        if passengers > self.capacity:
            print(f"Error: Passengers ({passengers}) exceed capacity ({self.capacity})")
            return 0
        total_fare = distance * self.fare_per_km * passengers
        return total_fare


# Example usage
if __name__ == "__main__":
    bus = Bus("City Bus", 50, 5)
    bus.display_info()
    
    distance = 20
    passengers = 30
    total = bus.calculate_total_fare(distance, passengers)
    print(f"Total fare for {passengers} passengers over {distance} km: ${total}")