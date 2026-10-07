class Student:
    # Class variable (shared by all objects)
    college = "jits"

    def __init__(self, name, branch):
        # Instance variables (unique to each object)
        self.name = name
        self.branch = branch

    @classmethod
    def new_college(cls, newname):
        # Class method → changes the class variable for all objects
        cls.college = newname

    @staticmethod
    def marks(a):
        # Static method → independent utility, checks pass/fail
        if a >= 40:
            print("pass")
        else:
            print("fail")


# ------------------- Testing -------------------

# Create an object (instance of Student)
s1 = Student("Vishnu", "CSE")

# Access instance variables and class variable
print(s1.name, s1.branch, s1.college)   # Vishnu CSE jits

# Class method usage
print("Before:", Student.college)       # jits
Student.new_college("Kaka")             # change college name
print("After college name change:", Student.college)  # Kaka

# Static method usage with a list of marks
marks = [12, 231, 12, 12]
for i in range(len(marks)):
    Student.marks(marks[i])   # checks each mark for pass/fail
