import java.io.{BufferedWriter, File, FileWriter}

object WordCloud {
  def main(args: Array[String]): Unit = {
    val stopWordsHook = scala.io.Source.fromURL("https://drive.google.com/uc?export=download&id=1aomNvHf6dH2_tp3FTeg2AQZUgD8Vp84l")
    val stopWords = stopWordsHook.mkString.toUpperCase().split("\\s").map(_.trim)
    stopWordsHook.close()
    val dataHook = scala.io.Source.fromURL("https://archive.org/stream/maelstrom_rifters/maelstrom_djvu.txt")
    val data = dataHook.mkString
      .split("<pre>")(1)
      .split("</pre>")(0)
      .split("\n")
      .drop(185)
      .dropRight(1049)
      .mkString("\n")
      .split(" ")
      .map(_.trim)
      .map(_.toUpperCase) //First words in a sentence are still words. I don't want to make lennie clarke with "toLower"
      .filterNot(stopWords.contains(_))
      .filterNot(Seq("PETER", "WATTS", "I", "IT", "", "-").contains(_))
      .map(_.replaceAll("[',.;\":?/*]", ""))
      .groupBy(identity).mapValues(_.length) //group by me, create map with group size (neato)
      .toSeq.sortBy(- _._2)
    dataHook.close()
    print(data.length)
    data.foreach(println)
    val file = new File("exported.txt")
    val writer = new BufferedWriter(new FileWriter(file))
    for(datum <- data.take(80)){
      for (_ <- 1 to datum._2) {
        writer.write(datum._1+"\n")
      }
    }
    writer.close()
  }
}