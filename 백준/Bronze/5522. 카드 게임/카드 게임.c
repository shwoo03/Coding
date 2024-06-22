#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n;
	int sum = 0;

	for (int i = 0; i < 5; i++)
	{
		scanf("%d", &n);
		sum += n;
	}

	printf("%d", sum);

	return 0;
}