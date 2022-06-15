import math
math.inf
def evaluateCentroidIsLowest(heightmapMatrix, rowIndex, columnIndex):
    if (rowIndex-1) >= 0:
        overNum = heightmapMatrix[rowIndex-1][columnIndex]
    else:
        overNum = math.inf

    if (columnIndex-1) >= 0:
        leftNum = heightmapMatrix[rowIndex][columnIndex-1]
    else:
        leftNum = math.inf
    
    try:
        rightNum = heightmapMatrix[rowIndex][columnIndex+1]
    except:
        rightNum = math.inf

    try:
        underNum = heightmapMatrix[rowIndex+1][columnIndex]
    except:
        underNum = math.inf

    return [overNum, leftNum, rightNum, underNum]



def evaluatePosibleDirections(heightMapMatrix, startCoords):

    placesToGo = True
    startRow = startCoords[0]
    startColumn = startCoords[1]
    coordsVisited = []
    
   
    
    placesToVisit = [[startRow, startColumn]]
    
    while placesToGo:
        
        for placeToVisit in placesToVisit:

            startRow =  placeToVisit[0]
            startColumn = placeToVisit[1]

            directions = evaluateCentroidIsLowest(heightMapMatrix, placeToVisit[0], placeToVisit[1])
            coordsVisited.append([placeToVisit[0], placeToVisit[1]])
            upDirection, leftDirection, rightDirection, underDirection = directions

           
            if (leftDirection < 9) and ([placeToVisit[0], placeToVisit[1]-1] not in coordsVisited):
                
                startColumn = placeToVisit[1]- 1
                if heightMapMatrix[startRow][startColumn] != 9:
                    placesToVisit.append([startRow, startColumn])
                startColumn = placeToVisit[1]
                startRow = placeToVisit[0]
            if (rightDirection < 9) and ([placeToVisit[0], placeToVisit[1]+1] not in coordsVisited):
               
                startColumn =placeToVisit[1]+ 1

                if heightMapMatrix[startRow][startColumn] != 9:
                    placesToVisit.append([startRow, startColumn])
                startColumn = placeToVisit[1]
                startRow = placeToVisit[0]
            if upDirection < 9 and ([placeToVisit[0]-1, placeToVisit[1]] not in coordsVisited):
                
                startRow = placeToVisit[0] - 1
                if heightMapMatrix[startRow][startColumn] != 9:
                    placesToVisit.append([startRow, startColumn])
                startColumn = placeToVisit[1]
                startRow = placeToVisit[0]
            if underDirection < 9 and ([placeToVisit[0]+1, placeToVisit[1]] not in coordsVisited):
                
                startRow = placeToVisit[0] + 1
                if heightMapMatrix[startRow][startColumn] != 9:
                    placesToVisit.append([startRow, startColumn])
                startColumn = placeToVisit[1]
                startRow = placeToVisit[0]
            

            placesToVisitIter = placesToVisit[:]
            for placeToVisitCoord in placesToVisitIter:
                if placeToVisitCoord in coordsVisited:
                    placesToVisit.remove(placeToVisitCoord)


        if len(placesToVisit) == 0:
            placesToGo = False

    
    return([list(x) for x in set(tuple(x) for x in coordsVisited)])
    
def main(filename):

    heightmapFile = open(filename)
    heightmapMatrix = []
    for heightline in heightmapFile:
        heightmapMatrix.append(list(map(int, heightline.strip())))
    
    lowpointCoords = []
    lowpointList = []
    for rowIndex in range(len(heightmapMatrix)):
        for columnIndex in range(len(heightmapMatrix[0])):

            centerNum = heightmapMatrix[rowIndex][columnIndex]
            
            surroundingNumbers = evaluateCentroidIsLowest(heightmapMatrix, rowIndex, columnIndex)

            allAreLower = all(centerNum < surNum for surNum in surroundingNumbers)
            if allAreLower:
                lowpointCoords.append([rowIndex, columnIndex])
                lowpointList.append(centerNum+1)


    basinSizes = []
    for lowpointCoor in lowpointCoords:
        
        basinSizes.append(len(evaluatePosibleDirections(heightmapMatrix, lowpointCoor)))
    basinSizes.sort()
    basinResult = 1
    for number in basinSizes[::-1][0:3]:
        basinResult *= number

                



    return [sum(lowpointList), basinResult]


print(main("input.txt"))
