try :
    list = [1,2,3,4,5]
    print(list[9])
except IndexError:
    print("your index is not vaild")
except Exception as e:
    print("your error",e)
else :
    print(list[9])
finally:
    print("closed")


