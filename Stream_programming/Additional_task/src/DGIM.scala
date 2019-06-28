class DGIM (val N: Int) {
  /** Datar-Gionis-Indyk-Motwani
    *
    * Algorithm has been implemented according to:
    * http://cs.pwr.edu.pl/macyna/power.pdf
    * starting @page 49
    */

  def input(): Stream[Boolean]= {
    /** Returns string of bits
      *
      * In: None
      * Out: True or False, at random
      * First we need some kind of input. DGIM accepts 1s and 0s (bits) and can be used for example for frequency
      * or most common elements
      */
    scala.util.Random.nextBoolean() #:: input()
  }
  // We need to know the biggest possible bucket, it's size being log2(N)
  val maxSize: Int = math.ceil(math.log10(N)/math.log10(2.0)).asInstanceOf[Int]
  /* Our buckets will be stored as an array with N rows and 2 columns.
  This means that buckets[r][0] will store the timestamp of older bucket of size 2^r and buckets[r][1] of the newer one.
  If such bucket does not exist the field is filled with -1. Worth noticing we are only storing 2 * log2(N) ints
    */
  var buckets: Array[Array[Int]] = Array.ofDim[Int](maxSize, 2)
  for(i <- 0 until maxSize) {
    buckets(i)(0) = -1
    buckets(i)(1) = -1
  } // This is equivalent to assuming our stream so far was [0]*N
  def resolveBucketsRow(size: Int, ts: Int): Unit ={
    /** Each time a new bucket (new data being bucket of size zero, with ts 1) gets introduced one of the three happens:
      * 1) there is no bucket of this size -> buckets[size][0] = ts
      * 2) there is one such bucket -> buckets[size][1] = ts
      * 3) there are two such buckets -> they are joined together and introduced as a bucket of size size+1 and ts
      * of the fresher one (hence recursive call), buckets[size][0] = ts and [1] is emptied as -1
      */
    if(buckets(size)(0) == -1) buckets(size)(0) = ts
    else if(buckets(size)(1) == -1) buckets(size)(1) = ts
    else {
      buckets(size)(0) = ts
      resolveBucketsRow(size+1, buckets(size)(1))
      buckets(size)(1) = -1
    }
  }
  def moveWindow(value: Boolean): Unit ={
    for(i <- 0 until maxSize) {
      if(buckets(i)(0) != -1) buckets(i)(0) += 1
      if(buckets(i)(1) != -1) buckets(i)(1) += 1
      if(buckets(i)(0) == N) buckets(i)(0) = -1
      if(buckets(i)(1) == N) buckets(i)(1) = -1
    } // Our buckets get older and move out of the window
    if(value){
      resolveBucketsRow(0, 1)
    }
  }
  def queryDGIM(windowSize: Int): Double ={
    var result: Double = 0
    for(i <- 0 until maxSize){
      if(buckets(i)(0) < windowSize && buckets(i)(0) != -1){ //if bucket starts within window (and exist)
        if(buckets(i)(0)+math.pow(2, i) > windowSize){ //but ends outside
          result += math.pow(2, i)/2
        } else result +=  math.pow(2, i)/2 // otherwise whole bucket counts
      }
      if(buckets(i)(1) < windowSize && buckets(i)(1) != -1){ //repeat for other column
        if(buckets(i)(1)+math.pow(2, i) > windowSize){
          result += math.pow(2, i)/2
        } else result +=  math.pow(2, i)/2
      }
    }
    result
  }

}
object Test{
  def main(args: Array[String]): Unit = {
    val ob = new DGIM(128)
    println("log2 of size is: ", ob.maxSize)
    println("--- Testing initialisation ---")
    for(i <- 0 until ob.maxSize) {
      println(ob.buckets(i)(0), ob.buckets(i)(1))
    }
    println("--- Testing data insertion ---")
    1 to 1000 foreach {_ => ob.moveWindow(true)}
    for(i <- 0 until ob.maxSize) {
      println(ob.buckets(i)(0), ob.buckets(i)(1))
    }
    println("--- Testing data extraction ---")
    println(ob.queryDGIM(10))
    println(ob.queryDGIM(20))
    println(ob.queryDGIM(100))

  }
}