with open("W:\practice\python\chapter 7 file input and output\program\demoo.txt","w+") as file:
    file.write("hi vishnu")
    file.flush()
    file.seek(0)
    data = file.read()
    print(data)
