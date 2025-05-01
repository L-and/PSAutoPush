#include <stdio.h>


int main(void) {
	int i = 0, loopcnt;
	int a, b;
	scanf("%d", &loopcnt);
	for (i = 0; i < loopcnt; i++) {
		scanf("%d %d", &a, &b);
		if (a > 0 && b < 10) {
			printf("%d\n", a + b);
		}
	}

	return 0;
}