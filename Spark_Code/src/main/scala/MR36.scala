import org.apache.spark.{SparkConf, SparkContext}

object MR36 {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("MR Graph")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val data = sc.textFile("hdfs:///data/web-Stanford.txt")
      .flatMap(_.split("\\n"))
      .filter(_.head != '#')
      .map(_.split("\\t"))

    val outDegree = data.map(a => (a.head, 1)).reduceByKey(_ + _)
    val inDegree = data.map(a => (a.last, 1)).reduceByKey(_ + _)
    val avgOutDegree = outDegree.map(_._2).reduce(_ + _) // data.count()
    val avgInDegree = inDegree.map(_._2).reduce(_ + _) // data.count()

    //outDegree.take(10).foreach(println)
    print(avgInDegree, " ",avgOutDegree)
  }
}
