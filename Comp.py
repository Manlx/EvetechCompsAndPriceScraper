from GetModels import ReadModels
global Models
Models = ReadModels()
class Components:
    Name = ""
    Price = 0
    Model = ""
    Supplier = ''
    def __init__(self,name,price,SupplierName):
        self.Name = name
        self.Price = price
        self.Model = IdentifyModel(self.Name)
        self.Supplier = SupplierName
##    @classmethod
    def GetToString(self):
        return "Name: {}\nPrice: {}\nModel: {}\nSupplier: {}".format(self.Name,self.Price,self.Model,self.Supplier)
def IdentifyModel(Name):
    for x in Models:
        if (x in Name):
            break
    return x;
