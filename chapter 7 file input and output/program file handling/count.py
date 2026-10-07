# Open the file in read mode
with open(r"W:\practice\python\chapter 7 file input and output\program\demoo.txt", "r") as f:
    data = f.read()                  # Read the entire file content into a string
    print(data)                      # Print the raw data from the file

# Remove leading/trailing whitespace (like spaces or newlines)
cleaned1 = data.strip()

# Split the string into a list wherever a comma is found
# Example: "3,12,321" → ["3", "12", "321"]
val = cleaned1.split(",")

# Convert each string in the list into an integer
# Example: ["3", "12", "321"] → [3, 12, 321]
num = list(map(int, val))

# Counters for even and odd numbers
even = 0
odd = 0

print(num)  # Print the list of integers

# Loop through the list using indices
for i in range(len(num)):
    if num[i] % 2 == 0:              # Check if the number is divisible by 2
        print(f"even is {num[i]}")   # Print the even number
        even += 1                    # Increase even counter
    else:
        print(f"odd: {num[i]}")      # Print the odd number
        odd += 1                     # Increase odd counter

# Print the total counts
print(f"total even numbers {even}")
print(f"total odd numbers {odd}")

print("same problem we can solve in any method")
with open(r"W:\practice\python\chapter 7 file input and output\program\sample.txt", "w+") as f:
    dataa = f.write("132,21,31,23,2321,22")                  # Read the entire file content into a string
    print(data)
clear1 =data.strip()
clear2=data.split(",")
number =list(map(int,clear2))
even2 =0
odd2= 0

# Loop directly over the numbers in the list
for i in number:                       
    if i % 2 == 0:                   # Check if the current number is divisible by 2
        print(f"even is {i}")        # Print the number if it's even
        even2 += 1                    # Increase the even counter
    else:
        print(f"odd: {i}")           # Print the number if it's odd
        odd2 += 1                     # Increase the odd counter

# After the loop, print the total counts
print(f"total even numbers {even2}")  # Show how many even numbers were found
print(f"total odd numbers {odd2}")    # Show how many odd numbers were found

