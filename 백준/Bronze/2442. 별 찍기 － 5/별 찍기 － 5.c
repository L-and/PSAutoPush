#include <stdio.h>

int main(void)
{
	int n, i, j;

	scanf("%d", &n);

	for (i = 0; i < n; i++)
	{
		for (j = n; j > i+1; j--)
		{
			printf(" ");
		}
		for (j = 0; j <= 2*i; j++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}