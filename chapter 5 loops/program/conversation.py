num = int(input("enter the num:"))
 
while 0 < num: #this iteration condition the num become the zero the loop will end upon the loop is continues
    temp = num % 10 #its give last number of number
    print("last",temp)
    num= num//10 #here we removed the last number 
    print("remaing",num)

print("final remaing ",num)