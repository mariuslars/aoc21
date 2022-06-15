def getNumPaths(filename):

    caveFile = open(filename)
    cavePaths = []
    for path in caveFile:
        
        cavePaths.append(path.strip().split("-"))
    
    return cavePaths

for line in getNumPaths("input_ex.txt"):
    print(line)