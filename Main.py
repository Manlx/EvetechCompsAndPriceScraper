from Comp import Components
from EvetechScrapeGPU import CollectCompAndPrice
myComp= Components("LOL",56)
print(myComp.GetToString())
print(CollectCompAndPrice('https://www.evetech.co.za/components/nvidia-ati-graphics-cards-21.aspx',True))
