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
        elif direction == "up":
            depthCounter -= number
        else:
            depthCounter += number
        
        k += 1
        
    
    return(forwardCounter * depthCounter)



def calcCourseAim(file):

    courseFile = open(file)

    depthCounter = 0
    forwardCounter = 0
    aim = 0

    for step in courseFile:

        direction, raw_number = step.split()
        number = int(raw_number)
        
        if direction == "forward":
            forwardCounter += number
            depthCounter += aim * number

        elif direction == "up":
            aim -= number

        else:
            aim += number

    return(forwardCounter * depthCounter)

print(calcCourse("2.txt"))
print(calcCourseAim("2.txt"))