def countIncreases(filename):

    depthFile = open(filename)
    depthList = []
    listCounter = 0
    largerThanCounter = 0
    for line in depthFile:
        floatNumber = float(line)
        depthList.append(floatNumber)
        
        if floatNumber > depthList[listCounter - 1]:
            largerThanCounter += 1

        listCounter +=1

    return largerThanCounter

print(countIncreases("1.txt"))



def countIncreasesMA(filename):

    depthFile = open(filename)
    depthList = []
    maDepthList = []

    depthCounter = 0
    largerThanCounter = 0
    for line in depthFile:
        floatNumber = float(line)
        depthList.append(floatNumber)
    

    for listIndex in range(len(depthList)):
        MA3 = sum(depthList[listIndex:(listIndex + 3)])
        maDepthList.append(MA3)

        depthCounter += 1

        if MA3 > maDepthList[depthCounter-2]:
            largerThanCounter +=1

    return largerThanCounter
   
print(countIncreasesMA("1.txt"))