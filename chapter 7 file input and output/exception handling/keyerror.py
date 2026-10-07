# Program to handle KeyError in a dictionary

student = {
    "name": "Vishnu",
    "age": 21,
    "course": "Computer Science"
}

# Trying to access a key that may not exist
try:
    print("City:", student["city"])   # This will raise KeyError
except KeyError:
    print("KeyError: 'city' key not found in dictionary")

# Safer way using .get()
print("City (safe access):", student.get("city", "Not Available"))
