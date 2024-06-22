#include <stdio.h>

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);

	printf("%0.10lf", (double)a / b);

	return 0;
}
