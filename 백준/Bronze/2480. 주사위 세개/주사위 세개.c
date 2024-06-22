#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);

	if (a == b && b == c && c == a)
	{
		printf("%d \n", 10000 + (a) * 1000);
	}
	else if (a == b || b == c || c == a) 
	{
		if (a == b)
		{
			printf("%d \n", 1000 + a * 100);
		}
		else if (b == c)
		{
			printf("%d \n", 1000 + b * 100);
		}
		else
		{
			printf("%d \n", 1000 + c * 100);
		}
	}
	else
	{
		int max;
		if (a > b && a > c)
		{
			max = a;
		}
		else if (b > a && b > c)
		{
			max = b;
		}
		else if (c > a && c > b)
		{
			max = c;
		}

		printf("%d \n", max * 100);
	}

	return 0;
}