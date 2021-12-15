import math
math.inf
def findAroundCenter(coordMatrix, rowIndex, columnIndex):
    coordDict = {}
    #Vertical and horizontan
    if (rowIndex-1) >= 0:
        overNum = coordMatrix[rowIndex-1][columnIndex]
    else:
        overNum = math.inf
    
    coordDict[str(rowIndex-1)+str(columnIndex)] = overNum
    if (columnIndex-1) >= 0:
        leftNum = coordMatrix[rowIndex][columnIndex-1]
    else:
        leftNum = math.inf
    coordDict[str(rowIndex)+str(columnIndex-1)] = leftNum
    try:
        rightNum = coordMatrix[rowIndex][columnIndex+1]
    except:
        rightNum = math.inf
    coordDict[str(rowIndex)+str(columnIndex+1)] =rightNum
    try:
        underNum = coordMatrix[rowIndex+1][columnIndex]
    except:
        underNum = math.inf
    coordDict[str(rowIndex+1)+str(columnIndex)] = underNum
    #Diagonals

    if ((rowIndex - 1) >= 0) & ((columnIndex - 1) >= 0):
        
        topLeft = coordMatrix[rowIndex-1][columnIndex-1]
    else:
        topLeft = math.inf
    coordDict[str(rowIndex-1)+str(columnIndex-1)] = topLeft
    if (rowIndex-1) >= 0:
        try:
            topRight = coordMatrix[rowIndex-1][columnIndex+1]
        except:
            topRight = math.inf
    else:
        topRight = math.inf
    coordDict[str(rowIndex-1)+str(columnIndex+1)] = topRight
    if (columnIndex -1 ) >= 0:
    
        try:
            bottomLeft = coordMatrix[rowIndex+1][columnIndex-1]
        except:
            bottomLeft = math.inf
    else: 
        bottomLeft = math.inf
    coordDict[str(rowIndex+1)+str(columnIndex-1)] = bottomLeft
    try:
        bottomRight = coordMatrix[rowIndex+1][columnIndex+1]
    except:
        bottomRight = math.inf
    coordDict[str(rowIndex+1)+str(columnIndex+1)] = bottomRight
    #print(coordDict)
    
    #return [topLeft, overNum, topRight, rightNum, bottomRight, underNum, bottomLeft, leftNum]
    return coordDict

def flashCounter(filename, nSteps):
    flashCounter = 0
    
    initialStatisFile = open(filename)
    initialStateList = []
    for line in initialStatisFile:

        initialStateList.append(list(map(int, line.strip())))

    k = 0
    for _ in range(nSteps):
        simultanFlashCounter = 0
        k += 1
        currentStepDone = []
        currentUpdatedcoordsDone = []
        isStillFlashing = True
        #for _ in range(1):
        for rowIndex in range(len(initialStateList[0])):
            for colIndex in range(len(initialStateList[0])):
                if str(str(rowIndex) + str(colIndex)) not in currentStepDone:
                    initialStateList[rowIndex][colIndex] +=1
        
        while isStillFlashing:
            #print(k)
            

            #print("inpuiit list: ")
            #for line in initialStateList:
            #    print(line)
            for rowIndex in range(len(initialStateList[0])):
                for colIndex in range(len(initialStateList[0])):
                    if initialStateList[rowIndex][colIndex] == 10:
                        simultanFlashCounter += 1
                        flashCounter += 1
                        currentStepDone.append(str(rowIndex)+str(colIndex))
                        initialStateList[rowIndex][colIndex] = 0
                        plussOneDict = findAroundCenter(initialStateList, rowIndex, colIndex)
                        
                        for coords in plussOneDict:
                            #print(initialStateList[1][0])
                            #print(plussOneDict)
                            if "-" in coords:
                                continue
                            else:
                                #print(coords)
                                updateCoords = list(map(int, coords))
                                if len(updateCoords) == 2:
                                #print(updateCoords[0])
                                #print(updateCoords[1])
                                    if initialStateList[updateCoords[0]][updateCoords[1]] == 10:
                                        currentUpdatedcoordsDone.append(str(updateCoords[0])+str(updateCoords[1]))
                                        initialStateList[rowIndex][colIndex] = 0
                                        #flashCounter += 1
                                    if str(str(updateCoords[0]) + str(updateCoords[1])) not in (currentUpdatedcoordsDone+currentStepDone):
                                        initialStateList[updateCoords[0]][updateCoords[1]] +=1
                                        #flashCounter += 1

                                        #initialStateList[updateCoords[0]][updateCoords[1]] = 0
                                        #print("lol")
        
            
            whileConditionList = []
            for rowIndex in range(len(initialStateList[0])):
                    for colIndex in range(len(initialStateList[0])):
                        whileConditionList.append(initialStateList[rowIndex][colIndex] == 10)
            isStillFlashing = any(whileConditionList)
        if simultanFlashCounter == 100:
            print(k)
            #isStillFlashing = False
        if k == 100:
            print("number of flashes: ",flashCounter)
    return initialStateList
    #pass



if __name__ == "__main__":
    
    finished = flashCounter("input.txt", nSteps= 232)
    print("main program: ")
    for line in finished:
        print(line)


    
    