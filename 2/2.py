def calcCourse(file):

    courseFile = open(file)

    k = 0
    depthCounter = 0
    forwardCounter = 0

    for step in courseFile:

        direction, raw_number = step.strip().split()
        number = int(raw_number)
        
        if direction == "forward":
            forwardCounter += number
        if direction == "up":
            depthCounter -= number
        if direction == "down":
            depthCounter += number
        
    #    print("k", k)
        k += 1
      #  print(step.strip().split())
        
       # if k == 4:
        #    break
        
    
    return(forwardCounter * depthCounter)

#print(calcCourse("2.txt"))

def calcCourseAim(file):

    courseFile = open(file)

    k = 0
    depthCounter = 0
    forwardCounter = 0
    aim = 0

    for step in courseFile:
        #print(step.split())
        direction, raw_number = step.split()
        number = int(raw_number)
        
        if direction == "forward":
            forwardCounter += number
            depthCounter += aim * number

        if direction == "up":
            aim -= number

        if direction == "down":
            aim += number

        
        
        

    
    return(forwardCounter * depthCounter)

print(calcCourseAim("2.txt"))