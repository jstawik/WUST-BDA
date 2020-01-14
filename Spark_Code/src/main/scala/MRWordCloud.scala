import org.apache.spark.{SparkConf, SparkContext}

object MRWordCloud {
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("MR Word Cloud")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val book = sc.textFile("hdfs:///data/maelstrom.txt")
    val stopWords = sc.textFile("hdfs:///data/stopwords.txt").collect()
    val counts = book.flatMap(line => line.split(" "))
      .map { case x if stopWords.contains(x.toLowerCase()) => None; case x => x }
      .map(word => (word, 1))
      .reduceByKey(_ + _)
      .sortBy(x => -x._2)
    counts.collect().take(10).foreach(println)
  }
}