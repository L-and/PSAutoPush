#include <stdio.h>



int main(void) {

	int a,b;
	int b1, b2, b3;
	int res1;

	scanf("%d", &a);
	getchar();
	scanf("%d", &b);

	b1 = b / 100;
	b2 = (b / 10)-(b1*10);
	b3 = b -( b1 * 100 )-( b2 *10);
	
	printf("%d\n", a * b3);
	printf("%d\n", a * b2);
	printf("%d\n", a * b1);
	printf("%d\n", a * b);


	return 0;
}