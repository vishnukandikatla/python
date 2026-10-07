num = int(input("enter the num:"))
 
while 0 < num:
    temp = num % 10
    print("last",temp)
    num= num//10
    print("remaing",num)