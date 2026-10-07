class Student:
    college = "Jyothishmathi"

    def __init__(self, name, marks):  # Better: use __init__ instead of manual method
        self.name = name
        self.marks = marks

    def avg(self):
        return sum(self.marks) / len(self.marks)


# Creating single student
s = Student("Vishnu", [99, 77, 33])
print(s.name, s.avg())
print(s.college)

s= Student("rav", [99, 77, 33])
print(s.name, s.avg())
print(s.college)

stud = {Student("hari", [39, 77, 33]),
        Student("adi", [29, 77, 33]),
        Student("rb", [29, 77, 33]) 
}
for s in stud:
    print(s.name,s.avg())
