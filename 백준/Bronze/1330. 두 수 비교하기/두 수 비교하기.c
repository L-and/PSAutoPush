#include <stdio.h>



int main(void) {

	int a,b;
	
	scanf("%d %d", &a, &b);
	if (a >= -10000 && b <= 10000) {
		if (a < b) printf("<");
		else if (a > b) printf(">");
		else if (a == b) printf("==");

	}
	return 0;
}