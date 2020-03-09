library(ggplot2)
my_data <- read.table(file = "clipboard", 
                      sep = "\t", header=FALSE)
data=as.matrix(my_data)

(p <- ggplot(my_data) + geom_tile(aes(fill = rescale), colour = "white") + scale_fill_gradient(low = "white",high = "steelblue"))

data2 <- system2("crystals.exe", args = c(10, 1000, 2, 10))  
