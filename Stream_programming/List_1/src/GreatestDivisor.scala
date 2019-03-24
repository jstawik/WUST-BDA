object GreatestDivisor {
  def main(args: Array[String]): Unit = {
   var filtered_args : Set[Int] = Set()
    for ( arg <- args ){
      try{
        filtered_args += arg.asInstanceOf[Int]
      } catch{
        case ex: Exception => {
          println("Can't cast "+arg+" to Int")
        }
      }
    }
    print(filtered_args)
  }
}
