import scala.io.Source
import scala.util.control._
object BinarySearch{

def binsearch(nos:Array[Int], srno: Int,l:Int,r:Int) :Int ={


    var mid=(l+r)/2
    
    if(l>r)  {return -1;}
    
    else if(nos(mid)==srno)
          {return mid}
    else if(nos(mid)>srno)
          {binsearch(nos,srno,l,mid-1)}
    else
          {binsearch(nos,srno,mid+1,r)}

}

def main(args:Array[String]){


           
           // println("Enter no of elements in array:  ")
           // var n:Int=Console.readInt
            var nos= new Array[Int](n)
           // println("Now enter array elements:  ")
           // for(i <- 0 to n-1) {
           //          nos(i)=Console.readInt
           //         // println ("ii"+i)
           //    }
           var loop=new Breaks

          var n=0;
           var filename="abc.txt"
           var srno=0
           var flag=0
           try{
            loop.breakable{
            for(line<-Source.fromFile(filename).getLines()){
              if(line.equals("search")){
                  loop.break
                  flag=1
                }
                if(flag==1)
                    srno=line.toInt
              nos(n)=line.toInt
              n+=1
            }
          }
             
           }
           catch{
            case ex: Exception=> println("File not read")
           }
           // scala.util.Sorting.quickSort(nos)

      // println("Enter number to be searched for:  ")
      // var srno:Int=Console.readInt

      var posn:Int=binsearch(nos,srno,0,n-1)
      if(posn == -1)
       {println("Not found")}
      else
        {println("Found at position  "+(posn+1))}
      }

}

