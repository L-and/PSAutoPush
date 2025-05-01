#include <stdio.h>

int main(void) {
	int a=0, b=0;

	scanf("%d %d", &a, &b);

	if (a > 0 && b < 10) {
		printf("%d", a - b);
	}
	return 0;
}