from Comp import Components
from EvetechScrapeGPU import CollectCompAndPrice
myComp= Components("LOL",56)
print(myComp.GetToString())
print(CollectCompAndPrice('https://www.evetech.co.za/components/intel-amd-based-bundle-packs-42.aspx',True))
