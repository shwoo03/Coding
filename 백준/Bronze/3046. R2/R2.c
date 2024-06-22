#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int s,r1,r2;
    scanf("%d %d",&r1,&s);

    r2 = 2 * s - r1;
    printf("%d",r2);

	return 0;
}