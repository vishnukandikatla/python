list = [1,2,3,2,1]
copy = list.copy()
copy.reverse()
if (copy == list):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")