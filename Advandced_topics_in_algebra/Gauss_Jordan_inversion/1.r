gaussn <- function(x){
    #todo: 0 on a diagonal
    y = diag(nrow(x))
    for (i in 1:(nrow(x)-1)){
        if(x[i,i] == 0){
            x[,c(i,i+1)]<-x[,c(i+1,i)]
        }
    }
    if(x[nrow(x),nrow(x)] == 0){
        x[,c(nrow(x),0)]<-x[,c(0,nrow(x))]
    }
    for (i in 1:(nrow(x)-1)){
        x[i,] = x[i,]/as.vector(x[i,i])
        y[i,] = y[i,]/as.vector(x[i,i])
        for (j in (i+1):nrow(x)){
            x[j,] = x[j,]/as.vector(x[j,i])
            x[j,] = x[j,] - x[i,]
            y[j,] = y[j,]/as.vector(x[j,i])
            y[j,] = y[j,] - y[i,]
        }
    }
    for (i in nrow(x):2){
        x[i,] = x[i,]/as.vector(x[i,i])
        y[i,] = y[i,]/as.vector(x[i,i])
        for (j in (i-1):1){
            x[j,] = x[j,]/as.vector(x[j,i])
            x[j,] = x[j,] - x[i,]
            y[j,] = y[j,]/as.vector(x[j,i])
            y[j,] = y[j,] - y[i,]
        }
    }
    x[1,] = x[1,]/x[1,1]
    y[1,] = x[1,]/x[1,1]
    print(x)

}

