#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	char* c;
	int n;

	c = (char*)malloc(1000 * sizeof(char));
	c[0] = '\0';
	gets(c);
	scanf("%d", &n);


	printf("%c", c[n - 1]);

	return 0;
}