from SuppliersClass import Supplier
def GetInfos():
    Sups = []
    f = open('SupplierURLMethods.txt','r')
    for i in f:
        URLLoc = i.find('URL:')
        ProcLoc = i.find('Process:')
        Sups.append(Supplier(i[9:URLLoc],i[URLLoc+4:ProcLoc],i[ProcLoc+8:]))
    return Sups
