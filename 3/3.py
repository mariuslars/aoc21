def epgam(filename):

    bitFile = open(filename)

    zeroCounter = 0
    oneCounter = 0
    gamma = ""
    bitList = []
    for bitnumber in bitFile:

        stripedBitnumber = bitnumber.strip()
        bitList.append(stripedBitnumber)

    for i in range(len(stripedBitnumber)):
        
        for j in range(len(bitList)):
            
            number = bitList[j][i]
            
            if int(number) == 1:
                oneCounter += 1
            else:
                zeroCounter += 1

        if oneCounter > zeroCounter:

            gamma += "1"
        else:
            gamma += "0"

        zeroCounter = 0
        oneCounter = 0
    epsilon = ""
    for characterz in gamma:

        
        
        if characterz == "1":
            epsilon+=  "0"
        if characterz == "0":
            epsilon += "1"
    
    return int(gamma, 2)*int(epsilon,2)



def life_support_rating(filename, measure = "co2"):

    if measure == "co2":
        zeroWon = "1"
        oneWon = "0"
    else:
        zeroWon = "0"
        oneWon = "1"
    bitFile = open(filename)

    zeroCounter = 0
    oneCounter = 0

    bitList = []
    updatedBitList = []
    
    for bitnumber in bitFile:

        stripedBitnumber = bitnumber.strip()
        bitList.append(stripedBitnumber)

    for i in range(len(stripedBitnumber)):

        if len(bitList) == 1:
            
            return bitList 
        for j in range(len(bitList)):
            
            number = bitList[j][i]
            
            if int(number) == 1:
                oneCounter += 1
            else:
                zeroCounter += 1

        
        if oneCounter < zeroCounter:
            for entry in bitList:
                #print(entry)
                if str(entry)[i] == zeroWon:
                    updatedBitList.append(entry)
             
        elif oneCounter > zeroCounter:

            for entry in bitList:
                if str(entry)[i] == oneWon:
                    updatedBitList.append(entry)

        else:
            for entry in bitList:
                if str(entry)[i] == oneWon:
                    updatedBitList.append(entry)

        
        bitList = updatedBitList[:]                  
        updatedBitList = []
        oneCounter = 0
        zeroCounter = 0

def main():
    
    
    co21 = life_support_rating("3.txt", measure = "co2")
    ox1 = life_support_rating("3.txt", measure = "ox")
    epsgam = epgam("3.txt")
    print("epsiolGamma:",epsgam)
    print("oxCo2: ",int(co21[0], 2) * int(ox1[0], 2))
    

main() 