#include <stdio.h>

int main()
{
	int n;
	double total=0;
	int i;
	double ary[1000]={0,};
	double max=0;	
	double avg;
	
	scanf("%d",&n);
	
	for(i=0;i<n;i++)
	{
		scanf("%lf",&ary[i]);
		if(ary[i]>max) max=ary[i];
	}	


	for(i=0;i<n;i++)
	{
		ary[i]=ary[i]/max*100;
	}
	
	
	for(i=0;i<n;i++)
	{
		total+=ary[i];
	}
	
	
	avg=total/n;
	
	printf("%.2lf",avg);
	
	return 0;
}