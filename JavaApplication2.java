//package javaapplication2;
import java.io.*;
public class JavaApplication2
{
    public static void main(String args[])
    {
        JavaApplication2 ja=new JavaApplication2();
		BufferedReader br;
		int n,constraint,x=0;
		int weight[]=new int[20];
		int tradeoff[]=new int[20];
		int[][] cost=new int[20][20];
	    int dist[]=new int[10];
	    int answer;
	    int min1,min2,temp1=0,temp2=0;
	    String mst="";
		int i,j,previous[]=new int[20],cnt=0;
        try
		{
            br=new BufferedReader(new InputStreamReader(System.in));
            System.out.println("\n Enter number of vertices : ");
            n=Integer.parseInt(br.readLine());
            for(i=1;i<=n;i++)
                for(j=1;j<=n;j++)		
                    cost[i][j]=999;
	    	System.out.println("Enter adjacency matrix : ");
            for(i=1;i<=n;i++)
            {
                for(j=i+1;j<=n;j++)
                {
                    System.out.print("cost["+i+"]["+j+"] : ");
                    cost[i][j]=Integer.parseInt(br.readLine());
                    cost[j][i]=cost[i][j];
                    if(cost[i][j]==0)
						cost[i][j]=cost[j][i]=999;
                }
            }
            System.out.println("\n Enter weight for each node : ");
            for(i=1;i<=n;i++)
            {
                System.out.print("Node "+i+" : ");
                weight[i]=Integer.parseInt(br.readLine());
            }
            System.out.print("Enter weight  constraint : ");
            constraint=Integer.parseInt(br.readLine());	
            System.out.println("\n Weight Constraint : "+constraint);
            System.out.println("\n Adjacency matrix : ");
            for(i=1;i<=n;i++)
            {
                System.out.println();			
                for(j=1;j<=n;j++)
                {
                    System.out.print("\t"+cost[i][j]);
               	}
            }	
            int min=999,s=0;
            for(i=2;i<=3;i++)
            {
                min=999;
                for(j=i;j<=n;j++)
                {
                    temp1=cost[1][j];
                     if(temp1<min)
                    {
                        min=temp1;
                        s=j;
                    }
                }
                mst+="\n 1 to "+s;
            }            
            int mintradeoff=19;
            int visited[]=new int[20];
            int k;
            int a[]=new int[20];
            visited[1]=1;
            for(k=1;k<=4;k++)
            {
                System.out.println("\n--------------------------------------:Iteration "+k+":-----------------------------------");
                for(i=2;i<=n;i++)
                {
                    min=999;
                    for(j=2;j<=n;j++)
                    {
                        if(cost[i][j]<min)
                        {
                            min=cost[i][j];
                            x=j;
                        }
                    }
                    if(k==4&&i==5)
                    {
                        cost[(previous[1])][3]=dist[1];    
                    }
                    if(visited[i]!=1)
                        tradeoff[i]=min-cost[i][1];
                    else
                    {	
                        if(cost[(a[mintradeoff])][1]==0)
                        {
                            answer=ja.distance_to_root(i,n,cost);
                            tradeoff[i]=min-answer;   
                        }
                        else
                        {
                            tradeoff[i]=min-cost[(a[mintradeoff])][1];
                        }
                    }
                    System.out.println("Tradeoff["+i+"] : "+tradeoff[i]);
                    a[i]=x;
                }			
                min=999;			
                for(i=2;i<=n;i++)
                {
                    if(tradeoff[i]<min)
                    {
                        min=tradeoff[i];
                        mintradeoff=i;	
                    }
                }
                System.out.println("Minimum tradeoff : tradeoff("+mintradeoff+") : "+min);
                if((weight[mintradeoff]+weight[a[mintradeoff]])<=constraint&&visited[(a[mintradeoff])]!=1)
                {
                    //if(k<4)
                        //System.out.println("Edge from "+mintradeoff+" to "+a[mintradeoff]+" is selected..");                       
                    visited[mintradeoff]=1;
                    previous[cnt]=mintradeoff;
                    dist[cnt]=cost[mintradeoff][(a[mintradeoff])];
                    cnt++;
                    cost[mintradeoff][1]=0;
                    cost[1][mintradeoff]=0;
                    cost[mintradeoff][(a[mintradeoff])]=999;
                    cost[(a[mintradeoff])][mintradeoff]=999;
                    if(k<4)
                        mst+="\n"+mintradeoff+" to "+a[mintradeoff];
                }
                else
                {
                    System.out.println("Edge rejected...");
                    visited[mintradeoff]=0;
                }
            }
            System.out.println("\n\n Edged are selected in order : "+mst);
        }
        catch(Exception e)
        {
            System.out.println("\n Error occured........."+e);
        }
    }
        
    int distance_to_root(int i,int n,int cost[][])
    {
        System.out.println("IN FUNCTION ");
        int j,count=0;
        int c[]=new int[20];
        int distance[]=new int[10];
        int y=0;
        for(j=2;j<=n;j++)
        {
            if(cost[i][j]!=0&&cost[i][j]!=999)
            {
                if(cost[j][1]!=0)
                {
                    c[count]=cost[j][1]+cost[i][j];
                    distance[count]=cost[j][1];
                    count++;
                }
            }
        }
        int minimum=999;
        for(j=0;j<count;j++)
        {
            if(c[j]<=minimum)
            {
                minimum=c[j];
                y=j;
            }
        }
        System.out.println("Minimum value returned : "+distance[y]);
        return(distance[y]);
    }
}

/*OUTPUT:
kbw@kbw-Lenovo-G50-80:~/BE/cndm assignments-final$ javac JavaApplication2.java
kbw@kbw-Lenovo-G50-80:~/BE/cndm assignments-final$ java JavaApplication2 

 Enter number of vertices : 
6
Enter adjacency matrix : 
cost[1][2] : 5
cost[1][3] : 6
cost[1][4] : 9
cost[1][5] : 12
cost[1][6] : 15
cost[2][3] : 4
cost[2][4] : 3
cost[2][5] : 8
cost[2][6] : 10
cost[3][4] : 8
cost[3][5] : 5
cost[3][6] : 12
cost[4][5] : 6
cost[4][6] : 6
cost[5][6] : 7

 Enter weight for each node : 
Node 1 : 1
Node 2 : 1
Node 3 : 1
Node 4 : 1
Node 5 : 1
Node 6 : 1
Enter weight  constraint : 3

 Weight Constraint : 3

 Adjacency matrix : 

    999 5   6   9   12  15
    5   999 4   3   8   10
    6   4   999 8   5   12
    9   3   8   999 6   6
    12  8   5   6   999 7
    15  10  12  6   7   999
--------------------------------------:Iteration 1:-----------------------------------
Tradeoff[2] : -2
Tradeoff[3] : -2
Tradeoff[4] : -6
Tradeoff[5] : -7
Tradeoff[6] : -9
Minimum tradeoff : tradeoff(6) : -9

--------------------------------------:Iteration 2:-----------------------------------
Tradeoff[2] : -2
Tradeoff[3] : -2
Tradeoff[4] : -6
Tradeoff[5] : -7
Tradeoff[6] : -2
Minimum tradeoff : tradeoff(5) : -7

--------------------------------------:Iteration 3:-----------------------------------
Tradeoff[2] : -2
Tradeoff[3] : -2
Tradeoff[4] : -6
Tradeoff[5] : 0
Tradeoff[6] : -2
Minimum tradeoff : tradeoff(4) : -6

--------------------------------------:Iteration 4:-----------------------------------
Tradeoff[2] : -1
Tradeoff[3] : -2
Tradeoff[4] : 1
IN FUNCTION 
Minimum value returned : 6
Tradeoff[5] : 0
IN FUNCTION 
Minimum value returned : 5
Tradeoff[6] : 2
Minimum tradeoff : tradeoff(3) : -2


 Edged are selected in order : 
 1 to 2
 1 to 3
6 to 4
5 to 3
4 to 2
kbw@kbw-Lenovo-G50-80:~/BE/cndm assignments-final$ 

*/