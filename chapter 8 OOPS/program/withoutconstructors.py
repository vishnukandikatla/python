class Student:

    # Class variable
    # This is common for all Student objects
    college = "Jyothishmathi"

    # Normal method to store student details
    # We are NOT using __init__ constructor
    def details(self, name, marks):
        self.name = name      # Instance variable for name
        self.marks = marks    # Instance variable for marks

    # Method to calculate average marks
    def avg(self):
        return sum(self.marks) / len(self.marks)


# -----------------------------
# Creating first Student object
# -----------------------------

s = Student()

# Calling details() manually
s.details("Vishnu", [99, 77, 33])

# Printing student name and average
print(s.name, s.avg())

# Accessing class variable
print(s.college)


# -----------------------------
# Creating second Student object
# -----------------------------

s = Student()

# Giving details to the second student
s.details("Rav", [99, 77, 33])

print(s.name, s.avg())
print(s.college)


# -----------------------------
# Creating multiple Student objects
# -----------------------------

stud = {
    Student(),
    Student(),
    Student()
}

# Converting set into a list
students = list(stud)

# Giving details to each object
students[0].details("Hari", [39, 77, 33])
students[1].details("Adi", [29, 77, 33])
students[2].details("RB", [29, 77, 33])


# -----------------------------
# Printing all students
# -----------------------------

for s in stud:
    print(s.name, s.avg())