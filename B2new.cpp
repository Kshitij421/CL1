#include <iostream>
using namespace std;

int main()
{
	int cost[6][6],g1[8],g2[6][6],g3[6][6],v[5],minarr[8],visited[8];
	int i,j,k,min,calc;
#pragma omp parallel for
for(i=1;i<=4;i++)
{
	visited[i]=0;
}
for(i=1;i<=4;i++)
{
//#pragma omp parallel for
for(j=i+1;j<=4;j++)
{


	int m;
	cout<<"Enter cost of path between "<<i<<" and "<<j<<"=";
	cin>>m;
	cost[j][i]=cost[i][j]=m;

}
}
	

//Start traversing with vertex 1
#pragma omp parallel for
for(i=2;i<=4;i++)
{
	g1[i]=cost[i][1];
	cout<<"\ng1 : "<<i<<"= "<<g1[i];
}
#pragma omp parallel for
for(i=2;i<=4;i++)
{
#pragma omp parallel for
for(j=2;j<=4;j++)
{
if(j==i)
continue;
else
{
g2[i][j]=cost[i][j]+g1[j];
}

cout<<"\ng2 : "<<i<<","<<j<<" = "<<g2[i][j];
}

}
for(i=2;i<=4;i++)
{
min=999;
for(j=2;j<=4;j++)
{
if(j==i)
continue;
else
{
#pragma omp parallel for
for(k=2;k<=4;k++)
{
if(k!=i && k!=j)
{
g3[i][j]=cost[i][j]+g2[j][k];
}
}
}
if(g3[i][j]<min)
{
min=g3[i][j];
minarr[i]=g3[i][j];
v[i]=j;
}
cout<<"\ng3 : "<<i<<","<<j<<","<<(--k)<<" = "<<g3[i][j]<<"\n v["<<i<<"] = "<<v[i];
}
}
min=999;
#pragma omp parallel for
for(i=2;i<=4;i++)
{
calc=cost[1][i]+minarr[i];
cout<<"\ng3[1 ,"<<i<<"] = "<<calc;
if(calc<min)
{
min=calc;
g3[1][i]=calc;
v[1]=i;
}
}

i=1;j=1;
cout<<"\n";
while(visited[i]!=1)
{
cout<<i<<"-----";

visited[i]=1;
i=v[i];
}
#pragma omp parallel for
for(i=1;i<=4;i++)
{
if(visited[i]==0)
cout<<"-----"<<i;
}

cout<<"-----1"<<endl;
cout<<"Minimun Dist:"<<min;
return 0;
}


// -----OUTPUT---
// kbw@kbw-Lenovo-G50-80:~/BE/Execution A  group$ g++ B2new.cpp -o b2
// kbw@kbw-Lenovo-G50-80:~/BE/Execution A  group$ ./b2
// Enter cost of path between 1 and 2=8
// Enter cost of path between 1 and 3=4
// Enter cost of path between 1 and 4=10
// Enter cost of path between 2 and 3=9
// Enter cost of path between 2 and 4=40
// Enter cost of path between 3 and 4=50

// g1 : 
// g1 : 3= 4
// g1 : 4= 102= 8
// g2 : 2,3 = 13
// g2 : 2,4 = 50
// g2 : 3,2 = 17
// g2 : 3,4 = 60
// g2 : 4,2 = 48
// g2 : 4,3 = 54
// g3 : 2,3,-1 = 69
//  v[2] = 3
// g3 : 2,4,-2 = 94
//  v[2] = 3
// g3 : 3,2,-3 = 59
//  v[3] = 2
// g3 : 3,4,-4 = 98
//  v[3] = 2
// g3 : 4,2,-5 = 53
//  v[4] = 2
// g3 : 4,3,-6 = 67
//  v[4] = 2
// g3[1 ,
// g3[1 ,3] = 634] = 63
// g3[1 ,2] = 63
// 1-----3-----2----------4-----1
// Minimun Dist:63kbw@kbw-Lenovo-G50-80:~/BE/Execution A  group$ 
