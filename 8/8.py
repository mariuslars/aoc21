def fixSignal(file):

    signals = open(file)
    outputSignals = []
    inputSignals = []
    for signal in signals:

        outputSignals.append(signal.split("|")[1].strip().split(" "))
        inputSignals.append(signal.split("|")[0].strip().split(" "))
    
    TESTVAR = 0
    uniqueCounter = 0
    updatedOutput = []
    displayDict = {}
    for output in [inputSignals[TESTVAR]]:
        for number in output:
            
            sortedNumber = set(sorted(number))
            if len(number) in [2, 3, 4, 7]:
                uniqueCounter+=1
                if len(number) == 2:
                    en = sortedNumber
                    
                    print("1: ")
                    displayDict["".join(sorted(number))] = 1
                elif len(number) == 3:
                    
                    syv = sortedNumber
                    print("7: ", number)
                    displayDict["".join(sorted(number))] = 7
                elif len(number) == 4:
                    fire = sortedNumber
                    print("4: ", number)
                    displayDict["".join(sorted(number))] = 4
                elif len(number) == 7:
                    atte = sortedNumber
                    print("8: ", number)
                    displayDict["".join(sorted(number))] = 8
            else:
                updatedOutput.append(number)
        updatedOutput2 = []

        for number in updatedOutput:

            
            sortedNumber = set(sorted(number))
            #print(sortedNumber, ". ",syv <= sortedNumber, "lengde: ", len(sortedNumber) == 5)
            if (syv <= sortedNumber) and (len(sortedNumber) == 5):
                tre = sortedNumber
                print("3: ", number)
                displayDict["".join(sorted(number))] = 3
            else:
                updatedOutput2.append(number)
       # print("UPDATED1:", updatedOutput)
       # print("UPDATED2:",updatedOutput2)

        for number in updatedOutput2:
            sortedNumber = set(sorted(number))
            if len(sortedNumber.intersection(fire)) == 2:
                
                to = sorted(number)
                print("2: ", number)
                displayDict["".join(sorted(number))] = 2
                sortedNumber = set(sorted(number))
                #print(len(tre.difference(sortedNumber)) == 1)
                #print(len(sortedNumber.intersection(fire)))
                #print("inter: ", sortedNumber.intersection(fire))
                #print("rawnum: ",number)
                #print("fir: ",fire)
                #print("to: ",to)
                
                #return("LOL")


    #print("UPDATED2:",updatedOutput2)
    finalNumber = []
    print(displayDict)
    for number in outputSignals[TESTVAR]:
        print("LOL: ", number)
        sortnum = "".join(sorted(number))
        try:
            finalNumber.append(displayDict[sortnum])
        except:
            continue
    return finalNumber

print(fixSignal("8_ex.txt"))

" a\
b   c\
  d\
e   f\
  g"

#f = 9 unike
#e = 4 unike

#0 aller sist nulll.difference(set.intersection(to, tre, fire, fem))

#2 ETTER IDENTIFISERING AV 3: = 3 difference av 2 == 1, feks hvis 2 = {"a", "b", "c", "d"} og 3 = {"a", "b", "c", "e"}, da er 3.difference(2) == 1 (viktig med 3 først)


#5 Etter identifisering av 2 og 3: 8 difference av 5 == 2, 8.difference(2)
#6 Etter identifisering av 5, 8, 9: set.union(fem,atte.difference(ni))

#9 = innholdet i 4 + 2 bokstaver til #ETTER IDENTIFISERING AV 9


#1 direkte identifisert
#3 ETTER IDENTIFISERING AV 7: = innholdet i 7 + 2 bokstaver til 
#4 direkte identifisert
#7 direkte identifisert
#8 direkte identifisert


#if e + innhold i 4 = 


#0, 9 = innholdet i 7 + 3 bokstaver til