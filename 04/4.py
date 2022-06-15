class Bingo():

    def __init__(self):

        self._brettliste = []
        self._talliste = None

    def lesSpillbrett(self, filnavn):

        boardsFile = open(filnavn)
        listOfBoards = []
        board = []
        for line in boardsFile:

            
            if line == "\n":
                listOfBoards.append(Spillbrett(board))
                board = []
            else:
                board.append(line.strip().split())
                
        listOfBoards.append(Spillbrett(board))

        self._brettliste = listOfBoards

    def lesTrekkrekke(self, filnavn):
        drawnNumbersFile = open(filnavn)
        
        for line in drawnNumbersFile:
            drawnNumbers = line.split(",")

        self._talliste = drawnNumbers

    def hentAntallSpillbrett(self):

        return len(self._brettliste)

    def hentTalliste(self):

        return self._talliste

    def hentSpillbrett(self, brettindeks):

        return self._brettliste[brettindeks]

class Spillbrett():

    def __init__(self, linjeliste):

        self._linjeliste = linjeliste
    
    def __str__(self):

        return str(self._linjeliste)
    
    def tellRad(self):
        radTeller = 0
        radLengde = len(self._linjeliste[0])
        for rad in self._linjeliste:
            
            for tall in rad:

                if tall == ".":
                    radTeller += 1

                if radTeller == radLengde:
                    return True
            radTeller = 0
        return False

    def tellKolonne(self):
        kolonneTeller = 0
        radLengde = len(self._linjeliste[0])
        for radIndeks in range(radLengde):

            for kolonneIndeks in range(radLengde):

                if self._linjeliste[kolonneIndeks][radIndeks] == ".":
                    kolonneTeller += 1

                if kolonneTeller == radLengde:
                    return True
            kolonneTeller = 0
        return False
    
    def evaluerSpillbrett(self, trukketNummer):

        for linjeIndeks in range(len(self._linjeliste)):

            for tallIndeks in range(len(self._linjeliste[linjeIndeks])):

                if self._linjeliste[linjeIndeks][tallIndeks] == trukketNummer:
                    self._linjeliste[linjeIndeks][tallIndeks] = "."


        if self.tellKolonne() or self.tellRad():
            vinnerBrett = self._linjeliste
            #vinnerBrett.append(trukketNummer)
            return vinnerBrett
        else: 
            return False


def score_finder(winnerBoard, trukketTall):

    scoreMultiplier = trukketTall
    boardScore = 0
    for line in winnerBoard[0:5]:

        for number in line:

            if number == ".":
                pass
            else:
                boardScore += int(number)

    totalScore = int(boardScore) * int(scoreMultiplier)
    return totalScore

def main():

    bingo = Bingo()
    bingo.lesSpillbrett("4_boards.txt")
    bingo.lesTrekkrekke("4_nums.txt")
    spillbrettOversikt = []
    resultOutput = []
    for trukketTall in bingo.hentTalliste():

        for spillbretIndeks in range(bingo.hentAntallSpillbrett()):
            #print(spillbretIndeks)
            currentBingobrett = bingo.hentSpillbrett(spillbretIndeks).evaluerSpillbrett(str(trukketTall))

            if currentBingobrett != False:

                if spillbretIndeks not in spillbrettOversikt:
                    spillbrettOversikt.append(spillbretIndeks)
                
                if len(spillbrettOversikt) == bingo.hentAntallSpillbrett():

                    resultOutput.append(score_finder(currentBingobrett, trukketTall))
                    return resultOutput
                elif len(resultOutput) ==0:
                    resultOutput.append(score_finder(currentBingobrett, trukketTall))
print(main())







