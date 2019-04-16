#library(ggplot2)
#library(ggridges)
#library(ggExtra)
#library(gganimate)
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
rawAP <- AP[0:-1]
df <- data.frame(x=seq(1, length(rawAP)), y=rawAP)
#reg = lm(y ~ log(x), data=df)
#reg <- as.list(reg)$coefficients
#reg <- unname(reg)
#curve(reg[1]+reg[2]*log(x), add=TRUE)
plot(rawAP)
plot.frequency.spectrum(fft(rawAP))
rawAP <- rawAP - mean(rawAP)
plot.frequency.spectrum(fft(rawAP))
plot(rawAP)
trend <- lm(rawAP ~ (seq(1:length(rawAP))))
detrended.rawAP <- trend$residuals
plot(rawAP); abline(trend)



  
ds <- read.csv(file="c:/atia/sun_spots.csv", header=FALSE, sep =",")
#plot(ds)
plot.frequency.spectrum(fft(ds))
