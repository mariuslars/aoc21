def crabMissile(file, costly):


    def crabEQ(startpos, newpos, costly):
        changepos = abs(startpos - newpos)
        if costly:
            return changepos*(1+changepos)/2
        else:
            return changepos
        
    crabPos = [int(pos) for pos in open(file).readline().split(",")]

    currentFuel = max(crabPos)
    fuelCounter = 0
    
    horizontalDirection = 1
    currentLowest = 1e20

    for _ in range(currentFuel):

        for pos in crabPos:
            
            fuelCounter += crabEQ(pos, horizontalDirection, costly = costly)


        horizontalDirection += 1

        if fuelCounter < currentLowest:
            currentLowest = fuelCounter
            
        fuelCounter = 0


    return round(currentLowest)


print("Cheap moves: ",crabMissile("7.txt", costly = False))
print("Expensive moves",crabMissile("7.txt", costly = True))