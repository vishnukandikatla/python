num = int(input("Enter a number: "))
temp =list(map(int,str(num).split()))
power = len(temp)
toa= 0

for i in range(len(temp)):
    toa = toa + temp[i]** power
print(toa)
if toa == num:
    print("yes")
else:
    print("no")