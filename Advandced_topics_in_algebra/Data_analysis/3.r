#library(ggplot2)
#library(ggridges)
#library(ggExtra)
#library(gganimate)
library(pracma)


plot.frequency.spectrum <-function(X.k, xlimits=c(0,length(X.k)/2)) {
  #horizontal axis from zero to Nyquist frequency
  plot.data  <-cbind(0:(length(X.k)-1), Mod(X.k))
  plot.data[2:length(X.k),2] <-2*plot.data[2:length(X.k),2]
  plot(plot.data, t="h", lwd=2, main=""
       , xlab="Frequency (number of cycles in the time range)"
       , ylab="Strength"
       , xlim=xlimits, ylim=c(0,max(Mod(plot.data[,2]))))
}

# sins
t <- seq(from=0, to=1, by=0.01)
f.1 <- 2
wave.1 <- sin(2*pi*f.1*t)
ft.1 <- fft(wave.1)
f.2 <- 6
a.2 <- 0.5
wave.2 <- a.2*sin(2*pi*f.2*t)
ft.2 <- fft(wave.2)

plot(wave.1)
plot(wave.2)
plot(wave.1+wave.2)
plot(Mod(ft.1))

plot.frequency.spectrum(ft.1)
plot.frequency.spectrum(ft.1+ft.2)
# triangle
wave.3 <- t %% .5
plot(wave.3)
plot.frequency.spectrum(fft(wave.3))
# square
wave.4 <- sign(sin(2*pi*t*2))
plot(wave.4)
plot.frequency.spectrum(fft(wave.4))
# random
wave.5 <- t*0 + .1 * runif(101,-.5, .5)
plot(wave.5)
plot.frequency.spectrum(fft(wave.5))
  
AP <- AirPassengers
rawaP <- AP
# df <- data.frame(x=seq(1, length(rawAP)), y=rawAP)
#reg = lm(y ~ log(x), data=df)
#reg <- as.list(reg)$coefficients
#reg <- unname(reg)
#curve(reg[1]+reg[2]*log(x), add=TRUE)

plot(rawAP)   # , type="o"
plot.frequency.spectrum(fft(rawAP))

rawAPdeMeaned <- rawAP - mean(rawAP) #can also use detrend

plot(rawAPdeMeaned)
plot.frequency.spectrum(fft(rawAPdeMeaned))

# trend <- lm(rawAP ~ (seq(1:length(rawAP))))
# detrended.rawAP <- trend$residuals

# plot(rawAP); abline(trend)
# plot.frequency.spectrum(fft(rawAP))
rawAPlinDetrended <- detrend(rawAPdeMeaned)

plot(rawAPlinDetrended)
plot.frequency.spectrum(fft(rawAPlinDetrended))

decomposedAP <- decompose(AP)
plot(decomposedAP)

# --------------- 4 below ------------------

sum(AP^2) - sum(Mod(fft(AP))^2/length(AP)) #-1.862645e-09 counts as 0, right? :D

# --------------- 5 below ------------------

#Had to manually reformat the dates from %Y-%m to %Y-%m-%d because
#> ds$Month[1]
#[1] "1749-01"
#> as.Date(ds$Month[1])
#Error in charToDate(x) : 
#  character string is not in a standard unambiguous format
#> as.Date(ds$Month[1], format="%Y-%m")
#[1] NA
#> lct <- Sys.getlocale("LC_TIME"); Sys.setlocale("LC_TIME", "C")
#[1] "C"
#> as.Date(ds$Month[1], format="%Y-%m")
#[1] NA
#sed ftw tho
#  sed -i 's/,/-01,/' sun_spots.csv


ds <- read.csv(file="c:/atia/sun_spots.csv", header=TRUE, sep =",", stringsAsFactors=FALSE)
ds$Month <- as.Date(ds$Month)
filtDS <-  ds[complete.cases(ds),]
plot(ds)
plot(decompose(ds$Sunspots))
plot.frequency.spectrum(fft(filtDS$Sunspots), xlimits=c(0,150))
deMeanedDS <- filtDS$Sunspots - mean(filtDS$Sunspots)
plot.frequency.spectrum(fft(deMeanedDS), xlimits=c(0,150))
deTrendedDS <- detrend(deMeanedDS)
plot(deTrendedDS)
plot.frequency.spectrum(fft(deTrendedDS), xlimits=c(0,150))



