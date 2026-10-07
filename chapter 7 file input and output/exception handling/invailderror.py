try :
    n = int(input("enter the number"))
    print(n)
except IndexError :
    print("it is not a interger",n)
except Exception as e :
    print("this is your error",e)
else:
    print(n+n)
finally :
    print("excution completed ")