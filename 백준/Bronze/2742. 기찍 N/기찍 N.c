#include <stdio.h>


int main(void) {
	int i = 0, loopcnt;

	scanf("%d", &loopcnt);
	for (i = loopcnt; i >=1; i--) {
		printf("%d\n", i);
	}

	return 0;
}