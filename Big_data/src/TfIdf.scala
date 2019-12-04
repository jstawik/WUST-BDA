object TfIdf {
  def main(args: Array[String]): Unit = {
    val dataHook = scala.io.Source.fromURL("https://archive.org/stream/maelstrom_rifters/maelstrom_djvu.txt")
    val data = dataHook.mkString
      .split("<pre>")(1)
      .split("</pre>")(0)
      .split("\n")
      .drop(185)
      .dropRight(1049)
      .map(_.replaceAll("[',.;\":?/*]", ""))
      .map(_.toLowerCase)
      .map(_.replaceAll("\\s\\s+", ""))
      .mkString("\n")
      //.split("^\\d+")
    dataHook.close()
    //data.foreach(println)
    val chapters = data.split("\\d+").map(_.split(" ").groupBy(identity).mapValues(_.length.toDouble))
    val chTF = chapters.map(mi => mi.transform((_,v) => v/mi.values.sum))
    val allWords = chapters.flatMap(_.keySet).toSet
    val chCount = chapters.length
    val wIDF: Map[String, Double] = allWords.view.map(word => word -> math.log(chCount.toDouble/chapters.map(_.contains(word)).count(identity))).toMap
    val tfidf = chTF.map(mi => mi.transform((k, v) => v*wIDF.getOrElse(k, 0.0)))
    tfidf.foreach(println)
  }
}
