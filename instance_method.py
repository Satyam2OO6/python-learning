# Class with an instance method

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def display(self):
        print("Employee Name:", self.name)
        print("Salary:", self.salary)

    # Another instance method
    def increment_salary(self, amount):
        self.salary = self.salary + amount
        print("Updated Salary:", self.salary)


# Create an object
emp1 = Employee("Rahul", 30000)

# Call instance methods
emp1.display()
emp1.increment_salary(5000)