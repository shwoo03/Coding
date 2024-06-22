#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    int n;
    scanf("%d",&n);

    for(int i = 0; i < n; i++)
    {
        for(int space = 0; space < i; space++)
        {
            printf(" ");
        }

        for(int star = n * 2 - ((1+i) * 2); star >= 0; star--)
        {
            printf("*");
        }

        printf("\n");
    }

    for(int i = n; i > 1; i--)
    {
        for(int space = 0; space < (i-2); space++)
        {
            printf(" ");
        }

        for(int star = n * 2 - ((i - 1) * 2); star >= 0; star--)
        {
            printf("*");
        }

        printf("\n");
    }

    return 0;
}