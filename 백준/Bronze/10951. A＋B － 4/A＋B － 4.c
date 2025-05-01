#include <stdio.h>


int main(void) {
	int a, b,returnvalue;

	while (1) {
		returnvalue=scanf("%d %d", &a, &b);
	
		if (returnvalue == EOF) break;
		printf("%d\n", a + b);
	}

	return 0;
} 