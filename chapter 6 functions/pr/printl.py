def printlist(lst, index=0):
    # Base case: if index reaches the length of the list, stop recursion
    if index == len(lst):
        return
    else:
        # Print the current element and its index
        print(lst[index], index)
    
    # Recursive call: move to the next index
    return printlist(lst, index+1)

# Example list
mp = [1, 23, 2, 3, 2]
printlist(mp)
