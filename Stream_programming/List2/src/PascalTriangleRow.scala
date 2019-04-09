class PascalTriangleRow(val n: Int) {
  var row:Array[Int] = init(n)
  def init(n: Int): Array[Int] ={
    val ret: Array[Int] = new Array[Int](n)
    ret(0) = 1
    for(i <- 1 until n){
      for(j <- i to 1 by -1){
        ret(j) = ret(j) + ret(j-1)
      }
    }
    ret
  }
  def display(): Unit ={
    for(i <- row) print(i+" ")
  }
}

object TestP {
  def main(args: Array[String]): Unit = {
    val triangle = new PascalTriangleRow(args(0).toInt)
    for (arg <- args.slice(1, args.length)) {
      try {
        println(triangle.row(arg.toInt))
      } catch {
        case ex: Exception => println(f"$arg is not a valid index")
      }
    }
    println()
    triangle.display()
  }
}
