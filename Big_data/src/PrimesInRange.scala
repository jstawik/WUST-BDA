object PrimesInRange {
  def main(args: Array[String]): Unit = {
    def primeApprox(from: Int, to: Int): Double = to.toDouble/(math.log(to)-1) - from.toDouble/(math.log(from)-1)
    print(primeApprox(2^64, 2^64+1000))
  }
}
