#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int k,n,m;
    scanf("%d %d %d",&k,&n,&m);

    int total = k * n;
    if(total > m)
    {
        printf("%d \n",total-m);
    }
    else
    {
        printf("0");
    }

	return 0;
}