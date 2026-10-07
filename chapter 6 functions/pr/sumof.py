def calsum(n):
    if n == 0:   # base case
        return 0
    else:
        return n + calsum(n-1)

print(calsum(10))   

