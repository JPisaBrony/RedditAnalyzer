require("arules")
#wd = dirname(parent.frame(2)$ofile)
#setwd(wd)
dataFile = "./data/dataset.txt"
x = read.transactions(dataFile, format = c("basket"), rm.duplicates = TRUE)
suppValue = 1 / dim(x)[1] + 0.01 #min support > 1 per post
a = apriori(x, parameter = list(supp = suppValue))
write(a, file = "./data/output.txt")