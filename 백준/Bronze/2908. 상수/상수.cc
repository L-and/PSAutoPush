#include <stdio.h>

int change(int num)
{
	int first_digit=num%10;
	int mid_digit=(num/10)%10;
	int last_digit=num/100;
	
	return first_digit*100+mid_digit*10+last_digit;
}

int main()
{
	int num1,num2;
	
	scanf("%d %d",&num1,&num2);
	
	num1=change(num1);
	num2=change(num2);
	
	if(num1>num2) printf("%d",num1);
	else if(num1<num2) printf("%d",num2);
	else printf("%d",num1);
	
	return 0;
}