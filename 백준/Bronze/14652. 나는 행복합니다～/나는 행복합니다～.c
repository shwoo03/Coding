#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int n,m,k;
    scanf("%d %d %d",&n,&m,&k);

    int x = (k / m);
    int y = (k % m);

    printf("%d %d",x,y);

	return 0;
}