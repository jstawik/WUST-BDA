import org.apache.spark.{SparkConf, SparkContext}

object MRNumbers {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("MR Numbers")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val data = sc.textFile("hdfs:///data/digits.txt")
    val numbers = data.flatMap( part => part.grouped(8))
      .filter(_.forall(_.isDigit))
      .map(_.toInt)
    println(numbers.reduce(Seq(_, _).max))
    println(numbers.reduce(Seq(_, _).min))
    println(numbers.reduce(_ + _)/numbers.map(_ => 1).reduce(_ + _))
    val uniqueNumbers = numbers.distinct()
    println(uniqueNumbers.count(), numbers.count())
  }
}
//99999998
//18
//52
//(18126801,20000000)
