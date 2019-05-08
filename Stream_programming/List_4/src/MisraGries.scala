import scala.collection.mutable.Map

class MisraGries(val accu: Int) {
  val r = scala.util.Random
  def input(): Stream[Any]= {
    if(r.nextBoolean()) math.floor(r.nextGaussian()*5) #:: input() //wouldn't be too frequent otherwise
    else (r.nextGaussian()*5).asInstanceOf[Int] #:: input()}
  def misraGries(elems: Int): (Map[Int, Int], Map[Double, Int]) ={
    var I = Map[Int, Int]()
    var D = Map[Double, Int]()
    for(i <- input() take elems){
      if(i.isInstanceOf[Int]){
        val j = i.asInstanceOf[Int]
        if(I.keySet.contains(j)) I.update(j, I(j)+1)
        else{
          if(I.keys.size < accu){
            I.update(j, 1)
          }
          else{
            for(x <- I.keys) if(I(x) == 0) I -= x
          }
        }
      }
      else {
        val j = i.asInstanceOf[Double]
        if(D.keySet.contains(j)) D.update(j, D(j)+1)
        else{
          if(D.keys.size < accu){
            D.update(j, 1)
          }
          else{
            for(x <- D.keys) if(D(x) == 0) D -= x
          }
        }
      }
    }
    (I, D)
  }
}

object Test{
  def main(args: Array[String]): Unit = {
    val ob = new MisraGries(5)
    for(i <- ob.input() take 10)
      println(i)
    println(ob.misraGries(100))
  }
}
