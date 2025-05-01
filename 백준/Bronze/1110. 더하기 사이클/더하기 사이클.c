#include <stdio.h>


int main(void) {
	int input;
	int firstnum, secondnum;
	int addnum;
	int newnum=0;
	int loopcnt=0;

	scanf("%d", &input);

	firstnum = input / 10;
	secondnum = input % 10;

	do{
		addnum = firstnum + secondnum;
		newnum = secondnum * 10 + addnum % 10;
		loopcnt++;

		firstnum =newnum / 10;
		secondnum = newnum % 10;
	} while (input != newnum);

	printf("%d", loopcnt);

	return 0;
} 