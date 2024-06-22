#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int t;
    scanf("%d",&t);


    for(int i = 0; i < t; i++)
    {
        int temp;
        scanf("%d",&temp);
        for(int j = 0; j < temp; j++)
        {
            printf("=");
        }

        printf("\n");
    }

	return 0;
}