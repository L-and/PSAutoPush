#include <stdio.h>


int main(void) {
	int loop;
	int maxnum=-1000000, minnum=1000000;
	int num;
	int i;

	scanf("%d",&loop);
	for (i = 0; i < loop; i++)
	{
		scanf("%d", &num);
		if (num > maxnum) maxnum = num;
		if (num < minnum)minnum = num;
	}

	printf("%d %d", minnum, maxnum);

	return 0;
} 