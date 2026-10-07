def odd_even(num):
    if num % 2 == 0:
        print("give num is even")
    else:
        print("give num is odd")
       
odd_even(2)
print("recursive function")
def fact(n):
    if n==0:
        return 1
    else:
        n = n * fact(n-1)  #recursive using rfact 
        return n
m=fact(6)
print(m)
def fact_iter(v):
    result = 1
    for i in range (1,v+1):   # loop from 1 to n
        result *= i
    return result

print(fact_iter(6)) 

def fact_i(n):
    result = 1
    i = 1
    while i <= n:
        result = i * result
        i +=1
    return result 

print(fact_i(6))
print("reverse string")
def reve(n):
    return n [::-1]

l = reve("vishnu")
print(l)

def fab(n):
    a = 0
    b = 1
     
    for i in range(0,n+1): #fibonacci series using loops  
        c = a+b
        a = b
        b = c
        print(f"{i}={c}", end=" ")
    return c
    
print(fab(10))
print("recursive function")
def fabre(n):
    if n <= 1:
        return n
    else:
        return fabre(n-1) + fabre(n-2) #fibonacci series using recursion
    
for i in range(10):
    print(fabre(i,),end=" ")
 
