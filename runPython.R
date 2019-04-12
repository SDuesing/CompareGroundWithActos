setwd("C:/Users/duesing/PycharmProjects/CompareGroundWithACTOS/")
file = "test.csv"
type = "SMPS"
system(paste('python plotSizeDistActosAndGround.py ',file," ",type,sep=""), wait=T)
