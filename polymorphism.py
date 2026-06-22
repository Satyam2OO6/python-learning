# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child Class
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child Class
class Cat(Animal):
    def sound(self):
        print("Cat meows")


# Create objects
dog = Dog()
cat = Cat()

# Call overridden methods
dog.sound()
cat.sound()