# Class with a constructor

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Calling methods
car1.show_details()
car2.show_details()