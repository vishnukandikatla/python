list = [16,12,7,2,1,43]
num = set(list)
reverse = sorted(num,reverse=True)
print(reverse)
d = sorted(num)
print(d)
print("The largest number is:",reverse[0])
print("The second largest number is:",reverse[1])