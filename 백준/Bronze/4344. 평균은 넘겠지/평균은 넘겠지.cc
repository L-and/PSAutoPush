#include <stdio.h>

int main()
{
	int i,j,n;
	double stunum;
	int avg=0,total=0;
	int stuscr[1000]={0,};
	double aboveavg=0;
	double ratio=0;
	
	scanf("%d",&n);
	
	for(i=0;i<n;i++)
	{
		aboveavg=0; 
		total=0;
		
		scanf("%lf",&stunum);
		
		for(j=0;j<stunum;j++)
		{
			scanf("%d",&stuscr[j]);
			total+=stuscr[j];
		
		}
		avg=total/stunum;
		
		for(j=0;j<stunum;j++)
		{
			if(stuscr[j]>avg) aboveavg++;
		}
		ratio=(aboveavg/stunum*100);
		
		printf("%.3lf%%\n",ratio);
		
	}
	
	return 0;
	
}