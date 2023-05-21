# Define a class called 'Car'
class Car:
    # Constructor method
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to get car information
    def get_info(self):
        return f"Car: {self.brand} {self.model} ({self.year})"

    # Method to accelerate the car
    def accelerate(self):
        print(f"The {self.brand} {self.model} is accelerating!")

# Create instances of the 'Car' class
car1 = Car("Toyota", "Camry", 2021)
car2 = Car("Honda", "Civic", 2022)

# Access object attributes
print(car1.brand)  # Output: Toyota
print(car2.model)  # Output: Civic

# Call object methods
print(car1.get_info())  # Output: Car: Toyota Camry (2021)
car2.accelerate()  # Output: The Honda Civic is accelerating!
