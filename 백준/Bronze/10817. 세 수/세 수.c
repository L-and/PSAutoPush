#include <stdio.h>


int main(void) {
	int i = 0, j = 0;
	int ary[3];
	scanf("%d %d %d", &ary[0], &ary[1], &ary[2]);

	if (ary[0] >= 1 && ary[2] <= 100) {
		for (i = 0; i < 2; i++) {
			for (j = i+1; j < 3; j++) {
				if (ary[i] > ary[j])
				{
					int temp;					
					temp = ary[i];
					ary[i] = ary[j];
					ary[j] = temp;
				}
			}
		}
		printf("%d", ary[1]);
	}
	return 0;
}