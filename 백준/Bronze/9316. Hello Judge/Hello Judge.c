#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n;
    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        printf("Hello World, Judge %d!\n",i+1);
    }

	return 0;
}