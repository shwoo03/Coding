#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++) 
	{
		for (int j = n - i; j > 0; j--)
		{
			printf("*");
		}

		printf("\n");
	}

	return 0;
}