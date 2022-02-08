class Supplier():
    SupName = ''
    URL = ''
    ProcessNumber = -1
    def __init__(self,SupName,URL,ProcessNumber):
        self.SupName = SupName
        self.URL = URL
        self.ProcessNumber = int(ProcessNumber)
    def toString(self):
        return 'Supplier: {}\nURL: {}\nProcessNumber: {}'.format(self.SupName,self.URL,self.ProcessNumber)
