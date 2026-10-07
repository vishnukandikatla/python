def printlist(list,index = 0): 
    if index == len(list):
        return
    print(list[index],index)
    return printlist(list,index + 1)
city =[1,34,2,4,2,42]
l = printlist(city,0)
print(l) #doesn't return nothing because the function is not returning anything, it is just printing the values of the list.
