class Subsystemerror:

    def __init__(self):

        self.navSubsystem = []
        self.matchingDict = {"{": "}", "[": "]", "(": ")", "<": ">"}
        self.pairList = ["[]", "()", "{}", "<>"]
        self.leftList = ["[", "(", "{", "<"]
        self.rightList = ["]", ")", "}", ">"]
        
        self.scoreDict = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self.completeScoreDict = {")": 1, "]": 2, "}": 3, ">": 4}
        self.illegalCharacters = []
        self.completeScoreList = []

    def readSubsystem(self, filename):

        subFile = open(filename)

        for subLine in subFile:

            self.navSubsystem.append(subLine.strip())

    def removeCompletePairs(self):
        stillGotPairs = True
        while stillGotPairs:
            for lineIndex in range(len(self.navSubsystem)):
                for pair in self.pairList:
                    self.navSubsystem[lineIndex] = self.navSubsystem[lineIndex].replace(pair, "")

            if not any(pair in subline for pair in self.pairList for subline in self.navSubsystem):

                stillGotPairs = False
        

    def removeAndFindIllegalCharacters(self):
        subsystemIter = self.navSubsystem[:]
        for subLineIndex in range(len(subsystemIter)):
            for signIndex in range(len(subsystemIter[subLineIndex])-1):
                currentSign = subsystemIter[subLineIndex][signIndex]
                nextSign = subsystemIter[subLineIndex][signIndex+1]
                if (currentSign in self.leftList) and (nextSign in self.rightList):
                   
                    self.illegalCharacters.append(subsystemIter[subLineIndex][signIndex+1])

                    self.navSubsystem.remove(subsystemIter[subLineIndex])
                    break


    def finalizeIncompleteLines(self):
        rightSideList = ""
        
        score = 0
        for lineIndex in range(len(self.navSubsystem)):
            for character in self.navSubsystem[lineIndex]:
                
                rightSideList+=self.matchingDict[character]
            for character in rightSideList[::-1]:
                score = score*5 + self.completeScoreDict[character]

            self.navSubsystem[lineIndex] = self.navSubsystem[lineIndex]+rightSideList[::-1]
            self.completeScoreList.append(score)
            self.completeScoreList.sort()
            rightSideList = ""
            score = 0
        
        
    def getIllegalScore(self):
        score = 0
        for illegalCharacter in self.illegalCharacters:
            score += self.scoreDict[illegalCharacter]

        print("score part 1: ",score)

    def getCompleteScore(self):
        
        scoreListLen = len(self.completeScoreList)
        middleIndex = int((scoreListLen - 1)/2)
        print("score part 2: ",self.completeScoreList[middleIndex])
        

if __name__ == "__main__":
    error = Subsystemerror()
    error.readSubsystem("input.txt")
    error.removeCompletePairs()
    error.removeAndFindIllegalCharacters()
    error.getIllegalScore()
    error.removeCompletePairs()
    error.finalizeIncompleteLines()
    error.getCompleteScore()


