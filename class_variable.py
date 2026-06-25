class Student:
    school = "ABC School"  # Class variable

    def __init__(self, name):
        self.name = name    # Instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name)
print(s2.name)

print(s1.school)
print(s2.school)