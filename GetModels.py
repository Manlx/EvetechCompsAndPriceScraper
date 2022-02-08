def ReadModels(Verbose= False):
    Models = [];
    f = open("GPU Models.txt","r")
    for i in f:
        Models.append(i.strip('\n'))
    f.close();
    if Verbose:
        print(len(Models))
    return Models
