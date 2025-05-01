#include <stdio.h>



int main(void) {

	int a, b, c;
	int res1, res2, res3, res4;

	scanf("%d %d %d", &a, &b,&c);
	if ((a >= 2) && (c <= 10000)) {
		res1=((a + b) % c);
		res2 = ((a%c+b%c)%c);
		res3 = ((a*b)%c);
		res4 = (((a%c)*(b%c))%c);

		printf("%d\n%d\n%d\n%d\n", res1, res2, res3, res4);
	
	}
	return 0;
}