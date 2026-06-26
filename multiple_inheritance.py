# Parent Class 1
class Father:
    def father_skill(self):
        print("Father knows driving")


# Parent Class 2
class Mother:
    def mother_skill(self):
        print("Mother knows cooking")


# Child Class
class Child(Father, Mother):
    def child_skill(self):
        print("Child knows coding")


# Create object
c = Child()

# Call methods from all classes
c.father_skill()
c.mother_skill()
c.child_skill()