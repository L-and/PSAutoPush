#include <stdio.h>

int main() {

	char a, b;
	scanf("%d %d", &a,&b);

	if ((a > 0) && (b < 10)) {


		printf("%d", a + b);
	}
    return 0;
}