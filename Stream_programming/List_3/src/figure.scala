abstract class Figure{
  def getPerimeter(): Double
  def getArea(): Double
}

class Hexagon(side: Double) extends Figure{
  override def getPerimeter(): Double = side*6
  override def getArea(): Double = 1.5*math.sqrt(3)*math.pow(side, 2)
}

class Pentagon(side: Double) extends Figure{
  override def getPerimeter(): Double = side*5
  override def getArea(): Double = math.pow(side, 2)*math.sqrt(25+10*math.sqrt(5))/4
}

class Circle(radius: Double) extends Figure{
  override def getPerimeter(): Double = 2*math.Pi*radius
  override def getArea(): Double = math.Pi*math.pow(radius, 2)
}

abstract class Quadrangle() extends Figure{
}

class Square(side: Double) extends Quadrangle{
  override def getPerimeter(): Double = side*4
  override def getArea(): Double = math.pow(side, 2)
}

class Rectangle(width: Double, height: Double) extends Quadrangle{
  override def getPerimeter(): Double = height*2 + width*2
  override def getArea(): Double = height*width
}

class Rhombus(side: Double, angle: Double) extends Quadrangle{
  override def getPerimeter(): Double = side*4
  override def getArea(): Double = math.pow(side, 2)*math.sin(angle)
}


object Test{
  def main(args: Array[String]): Unit = {
    val hexagon = new Hexagon(5)
    println(hexagon.getArea())
    println(hexagon.getPerimeter())
  }
}
