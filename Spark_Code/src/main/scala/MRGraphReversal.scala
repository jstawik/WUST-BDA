import org.apache.spark.{SparkConf, SparkContext}
import scala.util.parsing.json._



object MRGraphReversal {
  def main(args: Array[String]): Unit = {
    val conf = new SparkConf().setAppName("MR Graph Reversal")
    val sc = new SparkContext(conf)
    sc.setLogLevel("ERROR")
    val graph = sc.parallelize(JSON.parseFull(sc.textFile("hdfs:///data/example_graph.txt").collect()(0))
      .get
      .asInstanceOf[List[List[Any]]].flatMap(edges => edges(1).asInstanceOf[List[Double]]
      .map(i => (i, edges.head)))
    ).map(element => (element._1, List(element._2)))
     .reduceByKey(_ ++ _)

    graph.collect().foreach(println)
  }
}
