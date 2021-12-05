x1 = 1
x2 = 3
y1 = 0
y2 = 2

class Ventmap():

    def __init__(self):

        self._emptyMap = []
        self._lines = []

    def readLines(self, filename):

        linesMapping = open(filename)
        allCoords = []
        for line in linesMapping:
            splitLines = line.strip().split("->")

            firstCoord = splitLines[0].split(",")
            secondCoord = splitLines[1].split(",")
            allCoords = [int(entry) for entry in firstCoord+secondCoord]
               
            self._lines.append(allCoords)

    def getDims(self):

        colDim = 0
        rowDim = 0
        for line in self._lines:
            maxReadCol = int(max([line[0], line[2]]))
            maxReadRow = int(max([line[1], line[3]]))
            if maxReadCol > colDim:
                colDim = maxReadCol

            if maxReadRow > rowDim:
                rowDim = maxReadRow
        
        return [colDim, rowDim]

    def genEmptyMap(self):
        
        mapDims = self.getDims()
        rowlist = []
        
        
        for cols in range(mapDims[0]+1):

            for rows in range(mapDims[1]+1):

                rowlist.append(0)
            
            self._emptyMap.append(rowlist)
            rowlist = []

    def populateHorDiagMap(self):

        usedLines = []
        for line in self._lines:

            colLength = abs(line[x1] - line[x2])
            rowLength = abs(line[y1] - line[y2])
            

            if ((colLength > 0) and (rowLength > 0)) or ((colLength == 0) and (rowLength == 0)):
                
                continue
            
            colNums = list(range(min(line[y1], line[y2]), max(line[y1], line[y2])+1))
            rowNums = list(range(min(line[x1], line[x2]), max(line[x1], line[x2])+1))

            if line[y1] > line[y2]:
                colNums = colNums[::-1]

            if line[x1] > line[x2]:
                rowNums = rowNums[::-1]

            for row in rowNums:
                
                for col in colNums:

                    self._emptyMap[col][row] += 1
            
            usedLines.append(line)
            copyEmpty = self._lines[:]
        
        for line in copyEmpty:
           
            if line in usedLines:
                
                self._lines.remove(line)
        
    
    def populateVertMap(self):

        for line in self._lines:
            
            colNums = list(range(min(line[y1], line[y2]), max(line[y1], line[y2])+1))
            rowNums = list(range(min(line[x1], line[x2]), max(line[x1], line[x2])+1))

            if line[y1] > line[y2]:
                colNums = colNums[::-1]

            if line[x1] > line[x2]:
                rowNums = rowNums[::-1]


            for rowIndex in range(len(rowNums)):

                self._emptyMap[colNums[rowIndex]][rowNums[rowIndex]] += 1
            
    def getPoints(self):
        scoreCounter = 0
        for line in self._emptyMap:
            for number in line:
                if number > 1:
                    scoreCounter += 1

        print("score er: ", scoreCounter)


def main():

    map1 = Ventmap()
    map1.readLines("5.txt")
    map1.genEmptyMap()
    map1.populateHorDiagMap()
    map1.getPoints()
    map1.populateVertMap()
    map1.getPoints()
 

main()