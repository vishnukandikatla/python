class car():
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def show(self):
        print("brand", self.brand,end=",")
        print("color", self.color)

data = [("hero","black"),("he","black"),("gid","black")]

for brand,color in data:
    s= car(brand,color)
    s.show()
