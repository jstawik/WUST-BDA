import scala.collection.mutable.Map

class MisraGries(val accu: Int) {
  val r = scala.util.Random
  def input(): Stream[Any]= {
    if(r.nextBoolean()) math.floor(r.nextGaussian()*5) #:: input() //wouldn't be too frequent otherwise
    else (r.nextGaussian()*5).asInstanceOf[Int] #:: input()}
  def misraGries(elems: Int): Map[Any, Int] ={
    val A: Map[Any, Int] = Map()
    for(i <- input() take elems){
      A get i match {
        case Some(a) => A + (i -> (a + 1))
        case None =>
          if(A.keys.size < accu-1) A + (i -> 1)
          else {
            A.mapValues(_ -1)
            for(i <- A.iterator) if(A(i) == 0) A -=  i
          }
        }
      }
    A
  }
}

object Test{
  def main(args: Array[String]): Unit = {
    val ob = new MisraGries(5)
    println(ob.misraGries(100))
  }
}
