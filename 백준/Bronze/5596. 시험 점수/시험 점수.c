#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int total_min, total_man;
    total_man = 0;
    total_min = 0;

    for(int i = 0; i < 4; i++)
    {
        int temp;
        scanf("%d",&temp);
        total_min += temp;
    }

    for(int i = 0; i < 4; i++)
    {
        int temp;
        scanf("%d",&temp);
        total_man += temp;
    }

    if(total_man > total_min)
    {
        printf("%d",total_man);
    }
    else if(total_man <= total_min)
    {
        printf("%d",total_min);
    }

	return 0;
}