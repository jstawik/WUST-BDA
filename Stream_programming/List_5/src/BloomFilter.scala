import java.security.MessageDigest
import java.util.zip.CRC32


class BloomFilter {
  implicit def toShort(x: Int): Short = x.toShort
  val limit = Short.MaxValue
  var filterState = Array.fill[Short](limit)(0)
  val crc = new CRC32
  val md5 = MessageDigest.getInstance("MD5")
  val sha1 = MessageDigest.getInstance("SHA1")

  def input(): Stream[String]= {
    util.Random.alphanumeric.take(10).mkString #:: input()
  }

  def readFromStream(): Unit ={
    val element: String = (input() take 1).mkString
    var hash = BigInt(element.getBytes()) % BigInt(limit)
    println("Simple modulo:", hash)
    filterState(hash.toInt) += 1
    hash = BigInt(md5.digest(element.getBytes())) % BigInt(limit)
    println("MD5:", hash)
    filterState(math.abs(hash.toInt)) += 1
    hash = BigInt(sha1.digest(element.getBytes())) % BigInt(limit)
    println("SHA-1:", hash)
    filterState(math.abs(hash.toInt)) += 1
    crc.update(element.getBytes())
    hash = crc.getValue() % limit
    println("CRC32:", hash)
    filterState(hash.toInt) += 1
  }

  def removeFromFilter(element: String): Unit ={
    var hash = BigInt(element.getBytes()) % BigInt(limit)
    println("Simple modulo:", hash)
    filterState(hash.toInt) -= 1
    hash = BigInt(md5.digest(element.getBytes())) % BigInt(limit)
    println("MD5:", hash)
    filterState(math.abs(hash.toInt)) -= 1
    hash = BigInt(sha1.digest(element.getBytes())) % BigInt(limit)
    println("SHA-1:", hash)
    filterState(math.abs(hash.toInt)) -= 1
    crc.update(element.getBytes())
    hash = crc.getValue() % limit
    println("CRC32:", hash)
    filterState(hash.toInt) -= 1
  }

}

object Test{
  def main(args: Array[String]): Unit = {
    val bf = new BloomFilter
    for(i <- 1 to 100){
      bf.readFromStream()
    }

  }
}
