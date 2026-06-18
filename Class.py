# Define a class
class Student:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Create an object of the class
student1 = Student("Alice", 20)

# Call the method
student1.display()