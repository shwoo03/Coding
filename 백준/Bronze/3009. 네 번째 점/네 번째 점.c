#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int x1,y1;
    int x2,y2;
    int x3,y3;
    scanf("%d %d %d %d %d %d",&x1,&y1,&x2,&y2,&x3,&y3);

    int x4, y4;
    if(x1 == x2)
        x4 = x3;
    else if(x2 == x3)
        x4 = x1;
    else
        x4 = x2;

    if(y1 == y2)
        y4 = y3;
    else if(y2 == y3)
        y4 = y1;
    else
        y4 = y2;
    
    printf("%d %d",x4,y4);

    return 0;
}