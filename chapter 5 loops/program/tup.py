nums= ("vishnu", "sai", "kumar", "reddy", "vishnu", "sai", "kumar", "reddy", "vishnu", "sai")
#traverse
index = 0 
v = "vishnu" 
while index < len(nums):
    if  nums[index] ==v: # checking the value at index is equal to v or not
        print("Found in index",index)
    index += 1