#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
	for(int i = 0; i < 3; i++)
    {
        int a,b,c,d,e,f;
        scanf("%d %d %d %d %d %d",&a,&b,&c,&d,&e,&f);

        int hour = d - a;
        int minute = e - b;
        int second = f - c;

        if(second < 0)
        {
            minute -= 1;
            second += 60;
        }

        if(minute < 0)
        {
            hour -= 1;
            minute += 60;
        }

        printf("%d %d %d \n",hour,minute,second);
    }

	return 0;
}