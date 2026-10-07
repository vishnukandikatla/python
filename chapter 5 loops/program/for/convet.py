num = int(input("Enter the num: "))   # take input number

remain = num // 10    # remove the last digit (keep the rest)
last = num % 10       # extract the last digit
power = 1             # start with place value = 1

# loop to calculate how many digits are in 'remain'
# each iteration multiplies power by 10
# and chops off one digit from remain
temp_remain = remain   # use a copy so we don't lose 'remain'
while temp_remain > 0:
    power = power * 10     # increase place value
    temp_remain = temp_remain // 10   # reduce digits one by one
# This power will incerase until the condition safied
# rebuild the rotated number
# last digit is shifted to the front using 'power'
temp = last * power + remain

print(temp)   # print the rotated number
