class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks}"

    def __len__(self):
        return self.marks


s = Student("Alice", 95)

print(s)
print(len(s))