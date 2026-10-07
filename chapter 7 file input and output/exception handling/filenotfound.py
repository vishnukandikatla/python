try:
    with open("vishnu.txt","r") as f:
     data= f.readline()
    
except FileNotFoundError:
   print("file is doesn't not exists")
else :
   print("give the daa of the file \n",data)
finally:
   print("here the dat you can acces the program")
