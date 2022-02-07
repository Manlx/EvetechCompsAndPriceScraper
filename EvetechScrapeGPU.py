from urllib.request import Request, urlopen
#Requests Website
def CollectCompAndPrice(URL,EnableVerbose):
    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode("utf8")
    Lines = webpage.split('\n')
    Count = 0;
    DeleteLines = 0;
    Looking = True;
    
    if (EnableVerbose):
        print(len(Lines))
    
    #Deletes Everything up to the Product listings
    while (Looking and DeleteLines < len(Lines)):
        Looking = not('<table id="ctl00_ContentPlaceHolder1_Component_List_V2_IDs1_dl_products" cellspacing="0" border="0" style="border-collapse:collapse;">' in Lines[DeleteLines])
        DeleteLines += 1
    for x in range(0,DeleteLines):
        Lines.pop(0)
        
    if (EnableVerbose):
        print(len(Lines))

    #Deletes Everything After the table of Products
    Looking = True;
    DeleteLines = 0
    while (Looking and DeleteLines < len(Lines)):
        Looking = not('</table>' in Lines[DeleteLines])
        DeleteLines += 1
    i = len(Lines) - DeleteLines
    for x in range(0,i):
       Lines.pop(DeleteLines)

    if (EnableVerbose):
        print(len(Lines))
    #Deletes All Empty Or Space Lines
    for x in range(0,len(Lines)):
        Lines[x] = Lines[x].strip()
    for x in range(len(Lines)-1,-1,-1):
        if (not(Lines[x])):
            Lines.pop(x)

    if (EnableVerbose):
        print(len(Lines))
    #Crops Product Names
    for x in range(len(Lines)-1,-1,-1):
        lblFound = Lines[x].find("lblName")
        if lblFound >= 0:
            Lines[x] = Lines[x][Lines[x].find('lblName')+9:Lines[x].find("</span>")]

    if (EnableVerbose):
        print(len(Lines))
    #Deletes HTML Cluter
    for z in ['br','tr','td','h2','h3','a ','div','li','span','table','r']:
        for x in range(len(Lines)-1,-1,-1):
            Temp = '</{}'.format(z)
            if Temp in Lines[x]:
                Lines.pop(x)
        for x in range(len(Lines)-1,-1,-1):
            Temp = '<{}'.format(z)
            if Temp in Lines[x]:
                Lines.pop(x)

    if (EnableVerbose):
        print(len(Lines))

    for z in ['On Special']:
        for x in range(len(Lines)-1,-1,-1):
            if z in Lines[x]:
                Lines.pop(x)

##    for x in range(len(Lines)-1,-1,-1):
##        if (not(Lines[x])):
##            Lines.pop(x)
    print(len(Lines))
    return Lines
