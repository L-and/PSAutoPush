#include <stdio.h>


int main(void) {
	int i = 0, loopcnt;
	int a, b;

	scanf("%d", &loopcnt);
	for (i = 1; i <=loopcnt; i++) {
		scanf("%d %d", &a, &b);

			printf("Case #%d: %d + %d = %d\n",i,a,b, a + b);
	
	}

	return 0;
}