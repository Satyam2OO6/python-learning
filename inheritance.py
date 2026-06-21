# Parent Class
class Animal:
    def eat(self):
        print("Animal is eating")


# Child Class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")


# Create object of child class
d = Dog()

# Access parent class method
d.eat()

# Access child class method
d.bark()