#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int h, m;
    scanf("%d %d",&h,&m);

    int c;
    scanf("%d",&c);

    m += c;
    h += (m / 60);
    m %= 60;

    while(1)
    {
        if(h > 23)
        {
            h -= 24;
        }
        else if(h < 24)
        {
            break;
        }
    }

    printf("%d %d",h,m);

    return 0;
}