object GreatestDivisor {
  def getDiv(x: Int): Int = {
    if( x == 1) return 1
    for( i <- 1 to (x-1)){
      if(x % (x-i) == 0) return (x-i)
    }
    return -1
  }
  def main(args: Array[String]): Unit = {
   var filtered_args : Set[Int] = Set()
    for ( arg <- args ){
      try{
        filtered_args += arg.toInt
      } catch{
        case ex: Exception => {
          println("Can't cast "+arg+" to Int")
        }
      }
    }
    for (arg <- filtered_args){
      println(arg + " : " + getDiv(arg))
    }
    print(filtered_args)
  }
}
