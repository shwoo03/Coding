#include <stdio.h>
#include <stdlib.h>


int main()
{
	int x;
	scanf("%d", &x);

	for (int i = 1; i < x + 1; i++)
	{
		printf("%d\n", i);
	}

	return 0;
}