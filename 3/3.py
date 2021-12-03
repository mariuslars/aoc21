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
print("epsiolGamma:",epgam("3.txt"))
def ox(filename):

    bitFile = open(filename)


    zeroCounter = 0
    oneCounter = 0

    bitList = []
    updatedBitList = []
    
    for bitnumber in bitFile:

        stripedBitnumber = bitnumber.strip()
        bitList.append(stripedBitnumber)
  
    bitDict = {}
    bitDict["0"] = bitList
    
   
    for i in range(len(stripedBitnumber)):

        if len(bitList) == 1:
            return bitList
        for j in range(len(bitList)):
            
            number = bitList[j][i]
            
            if int(number) == 1:
                oneCounter += 1
            else:
                zeroCounter += 1

        if oneCounter > zeroCounter:
            for entry in bitList:

                if str(entry)[i] == "1":
                    updatedBitList.append(entry)
             
        elif oneCounter < zeroCounter:

            for entry in bitList:
                if str(entry)[i] == "0":
                    updatedBitList.append(entry)

        else:
            for entry in bitList:
                if str(entry)[i] == "1":
                    updatedBitList.append(entry)

        
        bitList = updatedBitList[:]                
        updatedBitList = []
        oneCounter = 0
        zeroCounter = 0


def co2(filename):

    bitFile = open(filename)

    zeroCounter = 0
    oneCounter = 0

    bitList = []
    updatedBitList = []
    
    for bitnumber in bitFile:

        stripedBitnumber = bitnumber.strip()
        bitList.append(stripedBitnumber)

    bitDict = {}
    bitDict["0"] = bitList
    
   
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
                if str(entry)[i] == "1":
                    updatedBitList.append(entry)
             
        elif oneCounter > zeroCounter:

            for entry in bitList:
                if str(entry)[i] == "0":
                    updatedBitList.append(entry)

        else:
            for entry in bitList:
                if str(entry)[i] == "0":
                    updatedBitList.append(entry)

        
        bitList = updatedBitList[:]                
        updatedBitList = []
        oneCounter = 0
        zeroCounter = 0


print("oxCo2: ",int(ox("3.txt")[0], 2)*int(co2("3.txt")[0], 2))