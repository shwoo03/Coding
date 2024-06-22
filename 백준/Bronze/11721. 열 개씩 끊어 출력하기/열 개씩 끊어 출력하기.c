#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int main()
{
    char arr[200];
    scanf("%s",arr);

    for(int i = 0; i < strlen(arr); i++)
    {
        printf("%c",arr[i]);
        if((i + 1) % 10 == 0 )
        {
            printf("\n");
        }
    }

    return 0;
}