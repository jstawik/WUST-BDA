class PrimeNumber (val n: Int){
  def calculatePrimeNumbers(): Set[Int]={
    def checkDivision(x: Int, s: Set[Int]): Boolean={
      for(element <- s){
        if(x%element == 0) return false
      }
      true
    }
    var ret : Set[Int] = Set()
    for( i <- 2 to n){
      if( checkDivision(i, ret)) ret += i
    }
    ret
  }
  def number(m: Int): Int ={
   calculatePrimeNumbers().toSeq.sorted.apply(m)
  }
}

object Test{
  def main(args: Array[String]): Unit = {
    val prime = new PrimeNumber(50)
    println(prime.calculatePrimeNumbers())
    println(prime.number(3))
  }
}