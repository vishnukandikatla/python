# Open the file in read mode
with open("W:\\practice\\python\\chapter 7 file input and output\\program\\demo.txt", "r") as f:
    text = f.read()  # Read the entire file content into a string
    print("before sorted the number", text)

# Initialize empty strings to collect different categories
collected = ""  # For digits (numbers)
char = ""       # For alphabetic characters
special = ""    # For special characters

# Loop through each character in the file content
for ch in text:
    if ch.isdigit():  # If the character is a digit
        collected = collected + ch + ","  # Add digit followed by a comma
    elif ch.isalpha():  # If the character is a letter
        char += ch  # Append to char string
    else:  # If the character is neither digit nor letter
        special += ch  # Append to special string

# Assign special characters to a variable for printing
spec = special
s = collected

# Print results
print("all number are here", s)  # Shows all digits separated by commas
print("extract charters", char)  # Shows all letters collected
print("special charaters", *spec, sep=",")  # Prints each special character separated by commas
