#include <stdio.h>


int main(void) {
	int maxnum,totalnum;
	int num;
	int i;
	scanf("%d %d",&totalnum,&maxnum);

	for (i = 0; i < totalnum; i++) {
		scanf("%d", &num);
		if (num < maxnum) printf("%d ", num);
	}

	return 0;
}