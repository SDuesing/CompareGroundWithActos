setwd("C:/Users/duesing/PycharmProjects/CompareGroundWithACTOS/")
file = "20150617_ground_aps+smps_merged.dat"
type = "SMPS"
system(paste('python plotSizeDistActosAndGround.py ',file," ",type,sep=""), wait=F)
