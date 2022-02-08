from Comp import Components
from EvetechScrapeGPU import CollectCompAndPrice
from WootwareScraper import CollectCompAndPriceWoot
from GetSupplierInfo import GetInfos

Funcs = [CollectCompAndPrice,CollectCompAndPriceWoot]
def LoadModelsFromURL(Verbose = False):
    Sups = GetInfos()
    Comps = []
    for s in Sups:
        Info = Funcs[s.ProcessNumber](s.URL)    
        Ready = False
        Name = ''
        Price = 0
        for z in Info:     
            if (Ready):
                Price = z
                Comps.append(Components(Name,Price,s.SupName))
            else:
                Name = z
            Ready = not(Ready)
        if(Verbose):
            for z in Comps:
                print(z.GetToString()+'\n')    
    return Comps
    
lol = LoadModelsFromURL()
for z in lol:
    print(z.GetToString())
