#include <stdio.h>


int main(void) {
	int ary[9];
	int maxnum;
	int local=1;
	int i;

	for (i = 0; i < 9; i++) {
		scanf("%d", &ary[i]);
	}

	maxnum = ary[0];

	for (i = 0; i < 9; i++) {
		if (maxnum < ary[i]) {
			maxnum = ary[i];
			local = i+1;
		}
	}
	printf("%d\n%d", maxnum, local);

	return 0;
} 