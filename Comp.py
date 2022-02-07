class Components:
    Name = ""
    Price = 0
    
    def __init__(self):
        print("Comp Created")
        self.Name = "Thicss"
        self.Price = 420
    def __init__(self,name,price):
        print("LOL")
        self.Name = name
        self.Price = price
##    @classmethod
    def GetToString(self):
        return "Name: {}\nPrice: {}".format(self.Name,self.Price)
