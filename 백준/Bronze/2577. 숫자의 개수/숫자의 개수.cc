#include <stdio.h>


int getdigit(int num)
{
	int i=1;
	int digit=1;
	
	while(1)
	{
	if(i<num){i*=10;digit++;}
	else break;
	}
	
	return digit;
}

int main()
{
	int A,B,C,D;
	int i;
	int num[10]={0,};
	int temp;
	int digit;
	
	scanf("%d %d %d",&A,&B,&C);
	
	D=A*B*C;
	
	digit=getdigit(D);
	
	for(i=0;i<digit-1;i++)
	{
		temp=D%10;
		D=D/10;
		
		switch(temp)
		{
			case 0:
				num[0]++;
				break;
			case 1:
				num[1]++;
				break;
			case 2:
				num[2]++;
				break;
			case 3:
				num[3]++;
				break;
			case 4:
				num[4]++;
				break;
			case 5:
				num[5]++;
				break;
			case 6:
				num[6]++;
				break;
			case 7:
				num[7]++;
				break;
			case 8:
				num[8]++;
				break;
			case 9:
				num[9]++;
				break;
			case 10:
				num[10]++;
				break;
	
		}
		
	}
	
	for(i=0;i<10;i++)
	{
		printf("%d\n",num[i]);
	}
	
	return 0;
	
}