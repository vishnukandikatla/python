# Create
student = {
    "name": "Vishnu",
    "age": 20,
    "marks": 95
}

print("Original:", student)

# Read
print("\nName:", student["name"])
print("Age:", student.get("age"))

# Add
student["city"] = "Hyderabad"
print("\nAfter Adding city:", student)

# Update
student["marks"] = 100
print("\nAfter Updating marks:", student)

# Check key
print("\n'name' exists?", "name" in student)

# Keys, Values, Items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# Iterate
print("\nIterating:")
for key, value in student.items():
    print(key, ":", value)

# Delete
student.pop("city")
print("\nAfter pop(city):", student)

# Copy
student_copy = student.copy()
print("\nCopy:", student_copy)

# Merge
student.update({"grade": "A"})
print("\nAfter update():", student)

# Length
print("\nLength:", len(student))

# Clear
student.clear()
print("\nAfter clear():", student)