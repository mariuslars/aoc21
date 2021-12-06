
fishPopulation <- function(filename, generations){
  
  initGens <- as.numeric(unlist(strsplit(readLines(filename), ",")))
  
  
  dd <- data.frame(age = initGens) %>% 
    group_by(age) %>% 
    summarise(n = n())
  
  for (i in 1:generations){
    #cat("\014", i)
    generateN8 <- generateN6 <- dd %>% filter(age == "0") %>% .$n
    
    if(any(dd$age == 0)){
      frame8 <- data.frame(age = 8, n = generateN8)
      frame6 <- data.frame(age = 6, n = generateN8)
    } else {
      frame8 <- data.frame(age = 8, n = 0)
      frame6 <- data.frame(age = 6, n = 0)
    }

    
    dd <- dd %>% 
      mutate(age = age-1) %>% 
      rbind(frame8) %>% 
      rbind(frame6) %>% 
      filter(age >= 0 & n > 0) %>% 
      group_by(age) %>% 
      summarise(n = sum(n)) %>% 
      arrange(age)
    
    
  }
  cat("\n\n\n")
  return(sum(dd$n))
}

main <- function(){
  #options(scipen = 9999)
  gen80 <- fishPopulation("6.txt", generations = 80)
  gen256 <- fishPopulation("6.txt", generations = 256)
  print(paste("fisk etter 80 generasjoner: ", gen80))
  print(paste("fisk etter 256 generasjoner: ", gen256))

    
}
main()
# 
# dd
# sum(dd$n)
# options(scipen = 99999)
# 
# sort(c(5,6,5,3,4,5,6,7,7,8))
# sort(c(4,5,4,2,3,4,5,6,6,7))
# 
# 
# initGens <- as.numeric(unlist(strsplit(readLines("6.txt"), ",")))
# newGen = function(x) {
#   if (x == 0){
#     x <- 6
#   } else {
#     x <- x -1
#   }
# }
# 
# 
# 
# fishEst <- function(initGen, numDays){
#   
#   notNew <- sum(initGen == 7)
#   initGen = sapply(initGen, FUN = newGen)
#   newFish <- 6 %in% initGen 
#   numNew <- sum(initGen == 6)
#   if (newFish){
#     initGen <- c(initGen, rep(8, numNew-notNew))
#   }
#   
#   day <<- day + 1
#   #  cat(day)
#   if (day == numDays){
#     return (length(initGen))
#   } else {
#     return (fishEst(initGen, numDays = numDays))
#   }
#   
# }
# initGen <- c(1, 7, 7, 6, 6)
# numDays <- 1
# day <<- 0;fishEst(initGens, 150);day <<- 0;
# 
# sapply(initGens, FUN = newGen)
# 
# 
# fishRec <- function(initGen, numDays){
#   
#   notNew <- sum(initGen == 7)
#   
#   
# }
# library(dplyr)
# 
# dd <- data.frame(age = initGens) %>% 
#   group_by(age) %>% 
#   summarise(n = n())
# i <- 1
# for (i in 1:256){
#   cat("\014", i)
#   generateN8 <- generateN6 <- dd %>% filter(age == "0") %>% .$n
#   
#   if(any(dd$age == 0)){
#     frame8 <- data.frame(age = 8, n = generateN8)
#     frame6 <- data.frame(age = 6, n = generateN8)
#   } else {
#     frame8 <- data.frame(age = 8, n = 0)
#     frame6 <- data.frame(age = 6, n = 0)
#   }
#   #dd <- dd
#   
#  dd <- dd %>% 
#     mutate(age = age-1) %>% 
#     rbind(frame8) %>% 
#     rbind(frame6) %>% 
#     filter(age >= 0 & n > 0) %>% 
#     group_by(age) %>% 
#     summarise(n = sum(n)) %>% 
#     arrange(age)
#   
#   
# }
# dd
# sum(dd$n)
# options(scipen = 99999)
# 
# sort(c(5,6,5,3,4,5,6,7,7,8))
# sort(c(4,5,4,2,3,4,5,6,6,7))
