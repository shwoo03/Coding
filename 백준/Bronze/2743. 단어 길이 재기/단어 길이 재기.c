#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	char* str;
	str = (char*)malloc(100 * sizeof(char));

	gets(str);
	printf("%d", strlen(str));

	free(str);

	return 0;
}