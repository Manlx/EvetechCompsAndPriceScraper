global Lines = []
import urllib.request


def ReadLines(Path):
    fp = urllib.request.urlopen(Path)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    Lines = mystr.split("\n")

def Strip(Values,Text):
    Out = []
    Temp = ""
    while (len(Text)> 0):
        CutoffVals = []
        CutoffVals.push()
        Cutoff = 0
        
        if ()
        Temp = Text[0:Text.index()]
        Out.push(Text.substring())

def FindClosestStr(Values,Text):
    Smallest = 0;

def Smallest(Value1,Value2):
    if (Value1>Value2):
        return Value2
    else:
        return Value1
