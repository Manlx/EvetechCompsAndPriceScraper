import requests
#Requests Website
def CollectCompAndPriceWoot(URL,EnableVerbose = False):
    Lines= requests.get(URL).text
    print(Lines)
    Count = 0;
    DeleteLines = 0;
    Looking = True;
    GPUNames = []
    GPUPrices = []
    LenLines = len(Lines)
    for z in range(0,LenLines):
        if ('<h2 class="product-name">' in Lines[z]):
            Temp = Lines[z+1]
            GPUNames.append(Temp[Temp.find('>')+1:Temp.find('<')])
    for z in range(0,LenLines):
        if ('class="price" id="product-price' in Lines[z]):
            Temp = Lines[z]
            GPUPrices.append(Temp[Temp.find('>')+2:Temp.find('<')])
    Outs = []
    LenLines = len(GPUNames)
    for z in range(0,LenLines):
        Outs.append(GPUNames[z])
        Outs.append(GPUPrices[z])
    return Outs
print(CollectCompAndPriceWoot("https://www.wootware.co.za/computer-hardware/video-cards-video-devices/shopby/in_stock_with_wootware?dir=asc&order=price"))
