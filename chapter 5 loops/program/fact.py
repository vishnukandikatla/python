i = 1 
fact = 1
num = int(input("Enter a number: "))
while i <= num:
       fact = fact * i
       i += 1
print("Factorial of ",num," is ",fact)