#include <stdio.h>

int main(void)
{
	int n, i, j;

	scanf("%d", &n);
	for (i = 0; i < n; i++)
	{
		if (i == n - 1)
			break;
		for (j = n; j > i + 1; j--)
		{
			printf(" ");
		}
		for (j = 0; j <= 2 * i; j++)
		{
			printf("*");
		}
		printf("\n");
	}

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < i; j++)
		{
			printf(" ");
		}
		for (j = 0; j < 2 * n - 2 * i - 1; j++)
		{
			printf("*");
		}
		printf("\n");
	}

	return 0;
}