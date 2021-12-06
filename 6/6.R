
fishPopulation <- function(filename, generations){
  
  initGens <- as.numeric(unlist(strsplit(readLines(filename), ",")))
  
  
  dd <- data.frame(age = initGens) %>% 
    group_by(age) %>% 
    summarise(n = n())
  
  for (i in 1:generations){
    
    generateN <-  dd %>% filter(age == "0") %>% .$n
    N <- ifelse(length(generateN) == 0, 0, generateN)
    frame8 <- data.frame(age = 8, n = N)
    frame6 <- data.frame(age = 6, n = N)
    
    dd <- dd %>% 
      mutate(age = age-1) %>% 
      rbind(frame8, frame6) %>% 
      filter(age >= 0 & n > 0) %>% 
      group_by(age) %>% 
      summarise(n = sum(n))
    
  }
  
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
