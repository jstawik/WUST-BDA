object HelloScala {
  def main(args: Array[String]): Unit = {
    println("Hello World!")
    for ( i <- args){
      println(i)
    }
  }
}