#include <stdio.h>

int main(void) {

	int a = 0, b=0;
	scanf("%d %d", &a,&b);

	for (;;) {
		if (a > b)
		{
			printf("Yes\n");
			scanf("%d %d", &a, &b);
		}
		else if ((a == 0) && (b == 0))
			break;
		else
		{
			printf("No\n");
			scanf("%d %d", &a, &b);
		}
	}
	return 0;
}