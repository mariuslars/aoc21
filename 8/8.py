def fixSignal(file):

    signals = open(file)
    outputSignals = []
    inputSignals = []
    for signal in signals:

        outputSignals.append(signal.split("|")[1].strip().split(" "))
        inputSignals.append(signal.split("|")[0].strip().split(" "))

    uniqueCounter = 0
    for input in outputSignals:
        for number in input:
        #s#ortedNumber = set(sorted(number))
            if len(number) in [2, 3, 4, 7]:
                uniqueCounter+=1

    
    updatedOutput = []
    displayDict = {}
    dictList = []
    scoreCounter = 0
    for output in inputSignals:
        for number in output:
            
            sortedNumber = set(sorted(number))
            if len(sortedNumber) in [2, 3, 4, 7]:
                #uniqueCounter+=1
                if len(number) == 2:

                    
                    
                    displayDict["".join(sorted(number))] = 1
                elif len(number) == 3:
                    
                    syv = sortedNumber
                    
                    displayDict["".join(sorted(number))] = 7
                elif len(number) == 4:
                    fire = sortedNumber
                    
                    displayDict["".join(sorted(number))] = 4
                elif len(number) == 7:
                    atte = sortedNumber
                    
                    displayDict["".join(sorted(number))] = 8
            else:
                updatedOutput.append(number)
        updatedOutput2 = []

        for number in updatedOutput:        
            sortedNumber = set(sorted(number))
            
            if (syv <= sortedNumber) and (len(sortedNumber) == 5):

                
                displayDict["".join(sorted(number))] = 3
            else:
                updatedOutput2.append(number)

        updatedOutput3 = []
        for number in updatedOutput2:
            sortedNumber = set(sorted(number))
            if len(sortedNumber.intersection(fire)) == 2:
                
                to = sorted(number)
                
                displayDict["".join(sorted(number))] = 2
            else:
                updatedOutput3.append(number)

        updatedOutput4 = []
        for number in updatedOutput3:
            sortedNumber = set(sorted(number))
            if len(atte.difference(sortedNumber)) == 2:
                
                fem = sorted(number)
                
                displayDict["".join(sorted(number))] = 5
            else:
                updatedOutput4.append(number)

        updatedOutput5 = []
        for number in updatedOutput4:
            sortedNumber = set(sorted(number))
           
            if len(fire.intersection(number))+2 == 6:
                
                ni = sorted(number)
                
                displayDict["".join(sorted(number))] = 9
            else:
                updatedOutput5.append("".join(sorted(number)))

        seks = set.union(set(fem),atte.difference(set(ni)))
   
    
        displayDict["".join(sorted(seks))] = 6

        updatedOutput5.remove("".join(sorted(seks)))

        zero = updatedOutput5[0]
        displayDict[zero] = 0

        dictList.append(displayDict)
        displayDict = {}
        updatedOutput5 = []
        updatedOutput4 = []
        updatedOutput3 = []
        updatedOutput2 = []
        updatedOutput = []

        
    finalNumber = []



    for indexer in range(len(dictList)):
        
        numberList = outputSignals[indexer]
        
        for number in numberList:
  
            sortnum = "".join(sorted(number))
            

            try: 
                finalNumber.append(str(dictList[indexer][sortnum]))
            except:
                continue
        #print(int("".join(finalNumber)))
        scoreCounter += int("".join(finalNumber))   
        finalNumber = []
    
    
    return [uniqueCounter, scoreCounter]
print(fixSignal("8.txt"))




#0 aller sist nulll.difference(set.intersection(to, tre, fire, fem))
#1 direkte identifisert
#2 ETTER IDENTIFISERING AV 3: = 3 difference av 2 == 1, feks hvis 2 = {"a", "b", "c", "d"} og 3 = {"a", "b", "c", "e"}, da er 3.difference(2) == 1 (viktig med 3 først)
#3 ETTER IDENTIFISERING AV 7: = innholdet i 7 + 2 bokstaver til 
#4 direkte identifisert
#5 Etter identifisering av 2 og 3: 8 difference av 5 == 2, 8.difference(2)
#6 Etter identifisering av 5, 8, 9: set.union(fem,atte.difference(ni))
#7 direkte identifisert
#8 direkte identifisert
#9 = innholdet i 4 + 2 bokstaver til #ETTER IDENTIFISERING AV 9


#if e + innhold i 4 = 


#0, 9 = innholdet i 7 + 3 bokstaver til