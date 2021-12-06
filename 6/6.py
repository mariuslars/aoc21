def fishEstimator(filsti, numDays):

    
    startGens = [int(age) for age in open(filsti).readline().split(",")]
    updatedGens = []
    day = 0
    
    for day in range(numDays):
        for ageIndeks in range(len(startGens)):

            if startGens[ageIndeks] == 0:
                startGens[ageIndeks] = 6
                startGens.append(8)
            else:
                startGens[ageIndeks] -= 1
                
    return len(startGens)


    
    

print(fishEstimator("6_ex.txt", 80))
#Works only for 80 gens. Way to slow for 256. Changed to R for this one..,.