library(ggplot2)
library(ggridges)
library(ggExtra)
library(gganimate)

data(ChickWeight)

ggplot(data=ChickWeight, aes(x= Time, weight)) + geom_point() + geom_rug(col="steelblue",alpha=0.5, size=1.5)
ggplot(data=ChickWeight, aes(x=weight, y=Time, color=Diet, size=Diet)) + geom_point() + theme(legend.position="none")
 ggplot(data=ChickWeight, aes(x=weight, group=Diet, fill=Diet)) + geom_density(adjust=1.5)