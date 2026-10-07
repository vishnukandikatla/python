class Car:
    def __init__(self, brand, color):   # constructor initializes attributes
        self.brand = brand
        self.color = color

    def show(self):                     # method prints attributes
        print("brand:", self.brand, end=",")
        print("color:", self.color)

# Creating objects
s = Car("Honda", "Black")
b = Car("Hero", "Green")

# Calling show() method
s.show()
b.show()
