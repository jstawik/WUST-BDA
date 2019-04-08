class PascalTriangleRow(val n: Int) {
  var row:Array[Int] = init(n)
  def init(n: Int): Array[Int] ={
    var ret: Array[Int] = new Array[Int](n)
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

object TestP{
  def main(args: Array[String]): Unit = {
    val triangle = new PascalTriangleRow(10)
    triangle.display()
  }
}
