library(dplyr)
#Testing recursive solution
fishPopulationRecursive <- function(populationCount, generations){
  
  N <- populationCount[populationCount$age == 0, "n"][[1]]
  
  populationCount <- populationCount %>% 
    mutate(age = age-1) %>% 
    rbind(tibble(age = 8, n = N), 
          tibble(age = 6, n = N)) %>% 
    filter(age >= 0 & n > 0) %>% 
    group_by(age) %>% 
    summarise(n = sum(n))
  
  if (generations == 1){
    return(sum(populationCount$n))  
  } else {
    generations = generations-1
    
    return(fishPopulation(populationCount, generations))  
  }
  
}

mainRecursive <- function(){
  popframe <- as.numeric(unlist(strsplit(readLines("6.txt"), ","))) %>% 
    tibble(age = .) %>% 
    group_by(age) %>% 
    summarise(n = n())
  #options(scipen = 9999)
  print(paste("fisk etter 80 gen: ", fishPopulationRecursive(popframe, generations = 80)))
  print(paste("fisk etter 256 gen: ", fishPopulationRecursive(popframe, generations = 256)))
  
}
start <- Sys.time()
mainRecursive()
Sys.time() - start


#Standard solution
fishPopulation <- function(filename, generations){
  
  populationCount <- as.numeric(unlist(strsplit(readLines(filename), ","))) %>% 
    tibble(age = .) %>% 
    group_by(age) %>% 
    summarise(n = n())
  
  for (i in 1:generations){
    
    N <- populationCount[populationCount$age == 0, "n"][[1]]
    
    populationCount <- populationCount %>% 
      mutate(age = age-1) %>% 
      rbind(tibble(age = 8, n = N), 
            tibble(age = 6, n = N)) %>% 
      filter(age >= 0 & n > 0) %>% 
      group_by(age) %>% 
      summarise(n = sum(n))
    
  }
  
  return(sum(populationCount$n))
}

main <- function(){
  #options(scipen = 9999)
  gen80 <- fishPopulation("6.txt", generations = 80)
  gen256 <- fishPopulation("6.txt", generations = 256)
  print(paste("fisk etter 80 generasjoner: ", gen80))
  print(paste("fisk etter 256 generasjoner: ", gen256))
  
  
}
start <- Sys.time()
main()
Sys.time() - start
