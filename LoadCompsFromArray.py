from Comp import Components
from EvetechScrapeGPU import CollectCompAndPrice
def LoadModelsFromURL(URL,Verbose = False):
    Info = CollectCompAndPrice(URL)
    Comps = []
    Ready = False
    Name = ''
    Price = 0
    for z in Info:     
        if (Ready):
            Price = z
            Comps.append(Components(Name,Price))
        else:
            Name = z
        Ready = not(Ready)
    if(Verbose):
        for z in Comps:
            print(z.GetToString()+'\n')
    return Comps
    
LoadModelsFromURL('https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx',True)
