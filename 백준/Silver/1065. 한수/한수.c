#include <stdio.h>

int get_gap(int n)
{
	int one_digit,ten_digit;
	
	ten_digit=(n%100)/10;
	one_digit=n%10;
	
	return (ten_digit-one_digit);
}

int hansu_cheak(int n,const int gap)
{
	if(n<10) return 0;
	
	int one_digit,ten_digit;
	int now_gap;
	
	now_gap=get_gap(n);
	
	if(now_gap==gap){hansu_cheak(n/10,gap);}
	else return 1;
}

int main()
{
	int n;
	int num_of_hansu=0;
	int cheak=-1;
	scanf("%d",&n);
	
	if(n<=99)
	{
		num_of_hansu=n;
	}
	else if(n<=1000)
	{
		num_of_hansu=99;
		for(int i=100;i<=n;i++)
		{
			cheak=hansu_cheak(i,get_gap(i));
			if(cheak==0) num_of_hansu++;
		}
	}
	
	printf("%d",num_of_hansu);
	
	return 0;
}