import org.apache.spark.rdd.RDD
import org.apache.spark.{SparkConf, SparkContext}

import scala.util.Random

object MRWordCloud_2 {
  def nextWords(words: RDD[((String, String), Int)], initWord: String, n: Int): List[String] = {
    def nextWord(previousWord: String) = {
      val ret = words.filter(element => element._1._1 == previousWord).take(5)
      ret(Random.nextInt(ret.length))._1._2
    }
    1.to(n).foldRight[List[String]](List(initWord)){(_, ret) => ret :+ nextWord(ret.last)} //fun fact: foldLeft resulted in memory leak
  }
  def main(args: Array[String]) {
    val conf = new SparkConf().setAppName("MR Word Cloud")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val book = sc.textFile("hdfs:///data/maelstrom.txt")
    val stopWords = sc.textFile("hdfs:///data/stopwords.txt").collect()
    val words = sc.parallelize(
        book.flatMap(line => line.split(" "))
          .filter(x => !stopWords.contains(x.toLowerCase()))
          .map(_.replaceAll("[',.;\":?/*\\s]", ""))
          .map(_.toLowerCase())
          .collect()
          .sliding(2)
          .toSeq)
      .filter(array => !array.contains(""))
      .filter(array => array.length == 2)
      .map(array => (array(0), array(1)))
      .map(shingle => (shingle, 1))
      .reduceByKey(_ + _)
      .sortBy(x => -x._2)
      //.filter(element => element._1._1 == "Lubin")
    //words.take(20).foreach(println)
    nextWords(words, "guilt", 30).foreach(println)
  }
}
// guilt innocence scope hundred meters shore shed told her you see barely days back inside head you see face full groupies online thread called retrieved fins sliced near-shore surf filtered
