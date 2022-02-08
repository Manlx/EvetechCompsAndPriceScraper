from GetModels import ReadModels
global Models
Models = ReadModels()
class Components:
    Name = ""
    Price = 0
    Model = ""
    def __init__(self,name,price):
        self.Name = name
        self.Price = price
        self.Model = IdentifyModel(self.Name)
##    @classmethod
    def GetToString(self):
        return "Name: {}\nPrice: {}\nModel: {}".format(self.Name,self.Price,self.Model)
def IdentifyModel(Name):
    for x in Models:
        if (x in Name):
            break
    return x;
