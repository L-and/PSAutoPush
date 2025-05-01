#include <stdio.h>


int main(void) {
	int i = 0, loopcnt;

	scanf("%d", &loopcnt);
	for (i = 0; i < loopcnt; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
	
			printf("%d\n", a + b);
		
	}

	return 0;
}