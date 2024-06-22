#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	int total_s = 0;
    for(int i = 0; i < 4; i++)
    {
        int temp;
        scanf("%d",&temp);
        total_s += temp;
    }

    int m = total_s / 60;
    total_s %= 60;
    int s = total_s;

    if(s >= 60)
    {
        m += 1;
        s -= 60;
    }

    printf("%d\n%d",m,s);

	return 0;
}