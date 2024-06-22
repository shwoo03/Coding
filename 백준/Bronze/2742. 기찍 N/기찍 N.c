#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n;
	scanf("%d", &n);

	for (int i = n; i > 0; i--)
	{
		printf("%d\n", i);
	}

	return 0;
}