#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
	int a, b, x, y;
    scanf("%d %d", &a, &b);
    if(a < b)
        printf("-1");
    else{
        x=(a+b)/2;
        y=(a-b)/2;
        if(x+y==a && x-y==b)
            printf("%d %d", x, y);
        else
            printf("-1");
    }
    return 0;
}