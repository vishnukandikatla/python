with open("W:\\practice\\python\\chapter 7 file input and output\\program\\demo.txt", "r") as f:
    text = f.read()  # Read the entire file content into a string
    print("before sorted the number", text)
current="" 
number=[]
for ch in text:
    if ch.isdigit():
     current+= ch
    else:
     if current!="":  #if current is not equal to return true
      number.append(current)# it used for when the comma and whitespace appears in the text directly the total number add to numbers
      current = "" # here the reseting containerwe


if current!="": #it is final check if in case consist of any number
    number.append(current)     
print(number)
