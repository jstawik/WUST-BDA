### Jakub Stawik
### 218715

# Task 35: 
Apply Map-Reduce twice to the book you used in Problem 1. Make a list of the five most-related words with the each word. By related words, we mean words that appear side by side(after removing stop-words).  Of course, you have to program this task in the Map-Reducemodel.Try to apply the received list to generate a random paragraph from your book.

# 0. Environment perparation
A docker image of Cloudera Quick Start machine has been pulled and deployed. For ease of use it's being started with a host filesystem subdirectory mounted. Since HDFS needs to be reinitialised after each reboot a bash script is used to speed the process up:
```bash
> docker pull cloudera/quickstart:latest
> docker run -v /home/tsar/code:/home/cloudera/code --hostname=quickstart.cloudera --privileged=true -t -i -p 8888 -p 7180 -p 80 jav8hadoop
>> hdfs dfs -mkdir /data
>> hdfs dfs -put /home/cloudera/code/WUST-BDA/Big_data/resources/maelstrom.txt /data
```
# 1. Data preparation
The text of Maelstrom by Peter Watts has been downloaded from free online resource and put into HDFS directory as seen above. It is then loaded into memory by Spark context's textFile method. Let's analyze the initialization on a line by line basis:
```scala
 1.  val words = sc.parallelize(
 2.          book.flatMap(line => line.split(" "))
 3.            .filter(x => !stopWords.contains(x.toLowerCase()))
 4.            .map(_.replaceAll("[',.;\":?/*\\s]", ""))
 5.            .map(_.toLowerCase())
 6.            .collect()
 7.            .sliding(2)
 8.            .toSeq)
 9.        .filter(array => !array.contains(""))
10.       .filter(array => array.length == 2)
11.       .map(array => (array(0), array(1)))
12.       .map(shingle => (shingle, 1))
13.       .reduceByKey(_ + _)
14.       .sortBy(x => -x._2)
```
In lines 2-5 we clean the text. We check for the stop words, lowercase everything (so that words at the beginning of the sentence are not treated as separate) and strip the text of punctuation. We then briefly convert the `RDD` to `Array` so that we can use the `.sliding(n)` method to shinglify the text and convert it back to `RDD` with `.parallelize` in line 1.  
We then filter out pairs containing empty `String`s and elements that are not pairs at all. Line 11 turns those 2 element `Array`s into `Tuple`s to enforce the length and line 12 assigns each pair 1 as a value. We then reduce by key to get count of each pair occurring in that particular order. We then sort those to keep the most popular at the top.
# 2. Sentence generation
I've created a function generating possible word sequences given a wordset prepared as above, a word that initiates our search and a number of words to return:
```scala
def nextWords(words: RDD[((String, String), Int)], initWord: String, n: Int): List[String] = {
    def nextWord(previousWord: String) = {
      val ret = words.filter(element => element._1._1 == previousWord).take(5)
      ret(Random.nextInt(ret.length))._1._2
    }
    1.to(n).foldRight[List[String]](List(initWord)){(_, ret) => ret :+ nextWord(ret.last)} //fun fact: foldLeft resulted in memory leak
  }
```
It uses a helper function that filters the wordset for pairs using the initial word, takes at most 5 such pairs and returns one of the possible next words at random.The main function folds over a range of integers completely ignoring them and accumulating words to be returned.
# 3. Room for improvements
This algorithm can be improved in a few possible ways:
- The randomisation could be weighted - the `nextWord` function could return the next word with probability proportional to the number of occurrences in main text.
- Removing the stopwords guarantees our outcome will **not** sound like an english phrase. A possible fix would be to count a chance for two words being divided by a stopword separately and with a chance inserting it back into the generated paragraph.
- Maelstrom is a second part of the Rifter Trilogy. We could possibly improve the generated sentences by including Starfish and  βehemoth - the remaining two pieces.
- There is a lot of filtering being done in nextWords. Some words are also highly probable to loop back - for example "Lennie" and "Clarke" are the name and surname of one of the protagonists. As such it's used in altering order making "Lenie" highly probable to be followed by "Clarke" and vice versa. This means our paragraph generating function can loop into returning "Lenie Clarke Lenie Clarke did (...)". This situation calls for two important improvements:  
    - loop prevention -  the word shouldn't be able to be picked again instantly or - possibly - within `n` next words
    - word caching - if a word is popular it possible followers could be cached in memory to avoid filtering the whole list for them again
# 4. An example run of the algorithm resulted in:
```
guilt innocence scope hundred meters shore shed told her you see barely days back inside head you see face full groupies online thread called retrieved fins sliced near-shore surf filtered
```
Part of this could be interpreted as:
Hundred meters shore shed (as in: left behind) told her: "you see barely the days back inside your head, you see the face-full groupies in an online thread that called for retrived fins and sliced the near-shore surf filtered for (...)
Or something like that.