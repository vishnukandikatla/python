class car():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def show(self):
        print("brand:",self.brand,end=",")
        print("color:",self.color)
s = car("honda","black")
b = car("hero","green")

s.show()
b.show()

        

        