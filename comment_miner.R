require("arules")
dataFile = file.choose()
setwd(dirname(dataFile))
x = read.transactions(dataFile, format = c("basket"), rm.duplicates = TRUE)
suppValue = 1 / dim(x)[1] + 0.01 #min support > 1 per post
a = apriori(x, parameter = list(supp = suppValue))
write(a, file = "associations.txt")