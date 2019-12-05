import scala.math.pow

object Collisions {
  def main(args: Array[String]): Unit = {
    def approxCollisions(bins: Double, balls: Double, treshold: Double) = {
      def factorial(n: Double): Double = n match {
        case 0 => 1
        case x => x * factorial(x-1)
      }
      1 - math.exp(pow(balls,treshold)*math.exp(-balls/bins)*pow((balls/(bins*(treshold+1))-1),(-1))*pow(bins,(1-treshold))*pow((factorial(treshold)),(-1)))
      //Source: https://math.stackexchange.com/questions/535868/probability-of-multiple-collisions-in-the-birthday-problem
    }
    approxCollisions(365, 25, 2)
  }
}
