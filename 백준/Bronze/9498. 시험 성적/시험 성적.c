#include <stdio.h>

int main(void){
	
	int input;
	
	scanf("%d",&input);
	
	if((input>=90)&&(input<=100))
	printf("A");
	else if((input>=80)&&(input<=89))
	printf("B");
	else if((input>=70)&&(input<=79))
	printf("C");
	else if((input>=60)&&(input<=69))
	printf("D");
	else
	printf("F");

	return 0;
}